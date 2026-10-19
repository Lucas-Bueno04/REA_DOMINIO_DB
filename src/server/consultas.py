"""Funções de consulta nomeadas sobre o banco da Domínio (somente leitura), prontas para virar ferramentas MCP.

Cada função: recebe o `Motor` (conexão, auditoria e validação de SELECT), valida os argumentos, executa consultas parametrizadas e devolve um
dicionário JSON-seguro com os números, de onde vieram e o que conferir. O catálogo `FUNCOES` descreve cada uma (nome, descrição, parâmetros)
para mapear em ferramentas MCP sem reescrever nada: `mcp_server.py` só precisa registrar `FUNCOES[nome]["executar"]`.

Regra: nada aqui escreve no banco; todo SQL é SELECT com valores como parâmetros.
"""
from __future__ import annotations

import calendar
import datetime

from server.motor import ErroUso, Motor, _coagir

B = "bethadba."


def _mes(competencia: str) -> tuple[datetime.date, datetime.date]:
    """'AAAA-MM' ou 'AAAA-MM-DD' -> (primeiro dia do mês, primeiro dia do mês seguinte)."""
    c = _coagir(competencia if len(str(competencia)) > 7 else f"{competencia}-01")
    if not isinstance(c, datetime.date):
        raise ErroUso("competencia deve estar no formato AAAA-MM (ou AAAA-MM-DD).")
    ini = c.replace(day=1)
    fim = (ini + datetime.timedelta(days=calendar.monthrange(ini.year, ini.month)[1]))
    return ini, fim


def _vigencia(alias_nota: str, coluna_data: str) -> str:
    """Condição que escolhe a vigência do acumulador em vigor na data da nota (a mais recente até a data)."""
    return (f"a.vigencia_acu = (SELECT MAX(v.vigencia_acu) FROM {B}efacumulador_vigencia v "
            f"WHERE v.codi_emp = {alias_nota}.codi_emp AND v.codi_acu = {alias_nota}.codi_acu AND v.vigencia_acu <= {coluna_data})")


def _n(v) -> float:
    return round(float(v or 0), 2)


# ===================================================================================== receita bruta do Simples Nacional
def receita_bruta_simples(m: Motor, empresa: int, competencia: str) -> dict:
    """Receita bruta do mês no Simples Nacional: recalcula a partir dos documentos e compara com a base que a Domínio apurou.

    Receita = saídas não canceladas + serviços não cancelados + cupons fiscais (CF-e) vigentes, todos de acumuladores que incidem sobre
    receita bruta (IREC_ACU = S, vigência em vigor na data do documento), menos as devoluções de venda lançadas em entradas com acumulador
    que incide sobre devolução (IDEV_ACU = S).
    Conferido contra efsdoimp_simples_nacional (imposto 44, linhas de detalhe): fecha ao centavo em 38 de 40 empresa/competências de uma
    amostra aleatória (scripts/conciliar_receita_simples.py)."""
    empresa = int(empresa)
    ini, fim = _mes(competencia)

    def run():
        s = m._sql(f"""SELECT COALESCE(SUM(CASE WHEN a.irec_acu = 'S' THEN n.vcon_sai ELSE 0 END), 0) AS receita,
                              COALESCE(SUM(n.vcon_sai), 0) AS valor_total, COUNT(*) AS documentos
                         FROM {B}efsaidas n LEFT JOIN {B}efacumulador_vigencia a ON a.codi_emp = n.codi_emp AND a.codi_acu = n.codi_acu AND {_vigencia('n', 'n.dsai_sai')}
                        WHERE n.codi_emp = ? AND n.cancelada_sai = 'N' AND n.dsai_sai >= ? AND n.dsai_sai < ?""", (empresa, ini, fim))[0]
        v = m._sql(f"""SELECT COALESCE(SUM(CASE WHEN a.irec_acu = 'S' THEN n.vcon_ser ELSE 0 END), 0) AS receita,
                              COALESCE(SUM(n.vcon_ser), 0) AS valor_total, COUNT(*) AS documentos
                         FROM {B}efservicos n LEFT JOIN {B}efacumulador_vigencia a ON a.codi_emp = n.codi_emp AND a.codi_acu = n.codi_acu AND {_vigencia('n', 'n.dser_ser')}
                        WHERE n.codi_emp = ? AND n.cancelada_ser = 'N' AND n.dser_ser >= ? AND n.dser_ser < ?""", (empresa, ini, fim))[0]
        c = m._sql(f"""SELECT COALESCE(SUM(CASE WHEN a.irec_acu = 'S' THEN i.valor_total ELSE 0 END), 0) AS receita,
                              COALESCE(SUM(i.valor_total), 0) AS valor_total, COUNT(DISTINCT h.i_cfe) AS documentos
                         FROM {B}efcupom_fiscal_eletronico_impostos i
                         JOIN {B}efcupom_fiscal_eletronico h ON h.codi_emp = i.codi_emp AND h.i_cfe = i.i_cfe
                         LEFT JOIN {B}efacumulador_vigencia a ON a.codi_emp = i.codi_emp AND a.codi_acu = i.codi_acu
                              AND a.vigencia_acu = (SELECT MAX(x.vigencia_acu) FROM {B}efacumulador_vigencia x WHERE x.codi_emp = i.codi_emp AND x.codi_acu = i.codi_acu AND x.vigencia_acu <= h.data_cfe)
                        WHERE i.codi_emp = ? AND h.situacao = 0 AND h.data_cfe >= ? AND h.data_cfe < ?""", (empresa, ini, fim))[0]
        d = m._sql(f"""SELECT COALESCE(SUM(CASE WHEN a.idev_acu = 'S' THEN n.vcon_ent ELSE 0 END), 0) AS devolucoes, COUNT(*) AS documentos
                         FROM {B}efentradas n LEFT JOIN {B}efacumulador_vigencia a ON a.codi_emp = n.codi_emp AND a.codi_acu = n.codi_acu AND {_vigencia('n', 'n.dent_ent')}
                        WHERE n.codi_emp = ? AND n.dent_ent >= ? AND n.dent_ent < ?""", (empresa, ini, fim))[0]
        calc = _n(s["receita"]) + _n(v["receita"]) + _n(c["receita"]) - _n(d["devolucoes"])
        ap = m._sql(f"""SELECT tipo_receita, SUM(basen) AS base, SUM(valorn) AS imposto, SUM(valor_devolucao_venda) AS devolucao
                          FROM {B}efsdoimp_simples_nacional
                         WHERE codi_emp = ? AND codi_imp = 44 AND data_sim = ? AND anexo = 0 GROUP BY tipo_receita ORDER BY tipo_receita""", (empresa, ini))
        r = {
            "empresa": empresa, "competencia": ini.isoformat()[:7],
            "recalculado": {
                "saidas": {"receita": _n(s["receita"]), "valor_total_documentos": _n(s["valor_total"]), "documentos": s["documentos"]},
                "servicos": {"receita": _n(v["receita"]), "valor_total_documentos": _n(v["valor_total"]), "documentos": v["documentos"]},
                "cupons_fiscais": {"receita": _n(c["receita"]), "valor_total_documentos": _n(c["valor_total"]), "documentos": c["documentos"]},
                "devolucoes_de_venda": {"valor": _n(d["devolucoes"]), "documentos": d["documentos"]},
                "receita_bruta": round(calc, 2),
            },
        }
        if not ap:
            r["apurado_pela_dominio"] = None
            r["situacao"] = "sem_apuracao"
            r["aviso"] = ("Não há apuração do Simples (imposto 44) para esta empresa e competência: a empresa pode não estar no Simples, a apuração pode não "
                          "ter sido calculada, ou a competência está fora do período. O valor recalculado é só a receita dos documentos.")
            return r
        base = round(sum(_n(x["base"]) for x in ap), 2)
        r["apurado_pela_dominio"] = {"base_calculo": base, "imposto": round(sum(_n(x["imposto"]) for x in ap), 2),
                                     "devolucao_venda": round(sum(_n(x["devolucao"]) for x in ap), 2),
                                     "por_tipo_receita": [{"tipo_receita": x["tipo_receita"], "base_calculo": _n(x["base"]), "imposto": _n(x["imposto"])} for x in ap]}
        dif = round(calc - base, 2)
        r["diferenca"] = dif
        r["situacao"] = "confere" if abs(dif) < 0.01 else "diverge"
        if r["situacao"] == "diverge":
            r["aviso"] = ("A receita recalculada difere da base apurada. Causas já vistas: apuração por regime de caixa (receita de serviços/vendas recebidas, não "
                          "emitidas — hipótese não confirmada), exclusões de substituição tributária ou ajustes manuais na apuração. Confira os acumuladores e "
                          "o parâmetro de regime da empresa.")
        return r

    return m._executar("receita_bruta_simples", {"empresa": empresa, "competencia": competencia}, run)


# ===================================================================================== perfil fiscal da empresa
def perfil_fiscal(m: Motor, empresa: int, data: str | None = None) -> dict:
    """Perfil fiscal da empresa numa data: regimes federal, estadual e municipal em vigor, impostos ativos e evidências do que a empresa realmente apura.

    O regime federal vem de efparametro_vigencia.rfed_par, cuja legenda NÃO está no banco: aqui é deduzida do cruzamento com as apurações (5 = lucro
    presumido, 4 e 2 = Simples; os demais códigos têm evidência fraca). Por isso a resposta traz `evidencias`: se há apuração do Simples (imposto 44)
    e de IRPJ nos 12 meses até a data, que confirmam ou contradizem o regime."""
    empresa = int(empresa)
    dia = _coagir(data) if data else datetime.date.today()
    if not isinstance(dia, datetime.date):
        raise ErroUso("data deve estar no formato AAAA-MM-DD.")

    def run():
        p = m._sql(f"""SELECT TOP 1 vigencia_par, descricao_par, rfed_par, rest_par, rmun_par, regime_recolhimento_par, lctb_par, fili_par, subst_par,
                              integraent_par, integrasai_par, integraser_par
                         FROM {B}efparametro_vigencia WHERE codi_emp = ? AND vigencia_par <= ? ORDER BY vigencia_par DESC""", (empresa, dia))
        if not p:
            raise ErroUso(f"Empresa {empresa} não tem parâmetros fiscais em vigor em {dia.isoformat()} (sem escrita fiscal ou vigência posterior).")
        p = p[0]
        imp = m._sql(f"""SELECT i.codi_imp, g.nome_imp, g.sigl_imp FROM {B}efparametro_vigencia_impostos i
                           LEFT JOIN {B}geimposto g ON g.codi_emp = i.codi_emp AND g.codi_imp = i.codi_imp
                          WHERE i.codi_emp = ? AND i.vigencia_par = ? ORDER BY i.codi_imp""", (empresa, p["vigencia_par"]))
        de = dia - datetime.timedelta(days=365)
        simples = m._sql(f"SELECT COUNT(*) AS n, MAX(data_sim) AS ultima FROM {B}efsdoimp_simples_nacional WHERE codi_emp = ? AND codi_imp = 44 AND basen > 0 AND data_sim >= ? AND data_sim <= ?", (empresa, de, dia))[0]
        irpj = m._sql(f"""SELECT COUNT(*) AS n, MAX(i.data_sim) AS ultima FROM {B}efsdoimp i JOIN {B}geimposto g ON g.codi_emp = i.codi_emp AND g.codi_imp = i.codi_imp
                           WHERE i.codi_emp = ? AND g.nome_imp LIKE '%IRPJ%' AND i.data_sim >= ? AND i.data_sim <= ?""", (empresa, de, dia))[0]

        def nome(dominio: str, cod):
            return m.doms.get(dominio, {}).get("valores", {}).get(cod)
        rfed = p["rfed_par"]
        forte = rfed in (2, 4, 5)
        r = {
            "empresa": empresa, "data": dia.isoformat(), "vigencia_em_uso": p["vigencia_par"].isoformat(), "descricao_vigencia": (p["descricao_par"] or "").strip(),
            "regime_federal": {"codigo": rfed, "significado": nome("regime_federal_fiscal", rfed), "confianca_da_legenda": "alta (por evidência dos dados)" if forte else "baixa"},
            "regime_estadual": {"codigo": p["rest_par"], "significado": nome("regime_estadual_fiscal", p["rest_par"])},
            "regime_municipal": {"codigo": p["rmun_par"], "significado": nome("regime_municipal_fiscal", p["rmun_par"])},
            "gera_lancamentos_contabeis": p["lctb_par"] == "S", "processa_filiais": p["fili_par"] == 2, "substituicao_tributaria": p["subst_par"] == "S",
            "integracao_contabil": {"entradas": p["integraent_par"], "saidas": p["integrasai_par"], "servicos": p["integraser_par"]},
            "impostos_ativos": [{"codigo": x["codi_imp"], "nome": (x["nome_imp"] or "").strip(), "sigla": (x["sigl_imp"] or "").strip()} for x in imp],
            "evidencias_12_meses": {
                "apuracao_simples_nacional": {"competencias": simples["n"], "ultima": simples["ultima"].isoformat() if simples["ultima"] else None},
                "apuracao_irpj": {"linhas": irpj["n"], "ultima": irpj["ultima"].isoformat() if irpj["ultima"] else None},
            },
        }
        avisos = []
        if rfed in (2, 4) and not simples["n"]:
            avisos.append("Regime do Simples (códigos 2 e 4) mas sem apuração do Simples nos últimos 12 meses: empresa inativa, mudou de regime ou apuração não calculada.")
        if rfed == 5 and simples["n"]:
            avisos.append("Regime 5 (lucro presumido) mas com apuração do Simples recente: confira a vigência dos parâmetros.")
        if not forte:
            avisos.append("A legenda deste código de regime federal não está no banco e a evidência é fraca; confirme pelas apurações (campo evidencias_12_meses) e pelo cadastro da empresa.")
        if avisos:
            r["avisos"] = avisos
        return r

    return m._executar("perfil_fiscal", {"empresa": empresa, "data": data}, run)


# ===================================================================================== situação do eSocial na competência
def situacao_esocial(m: Motor, empresa: int, competencia: str) -> dict:
    """Situação do eSocial da empresa numa competência: se a folha está fechada (S-1299), remuneração (S-1200) e pagamentos (S-1210) enviados, e pendências.

    Fechamento: vale o ÚLTIMO evento S-1298 (reabertura) ou S-1299 (fechamento) da competência — a competência pode ser fechada, reaberta e fechada de novo.
    Um evento está aceito quando tem número de recibo e `validado` = 1; resposta 202 é sucesso com advertência; 401/411 são rejeições. Pendências: eventos
    da empresa sem recibo ou aguardando ajuste (qualquer competência)."""
    empresa = int(empresa)
    ini, fim = _mes(competencia)

    def run():
        fech = m._sql(f"""SELECT TOP 1 e.i_dados_eventos, e.i_evento_esocial, e.numero_recibo, e.validado, e.data_criacao_registro, e.i_resposta
                            FROM {B}foesocial_dados_eventos e
                           WHERE e.codi_emp = ? AND e.i_evento_esocial IN (1298, 1299) AND e.competencia_calculo = ? ORDER BY e.i_dados_eventos DESC""", (empresa, ini))
        ev = m._sql(f"""SELECT e.i_evento_esocial, COUNT(*) AS enviados,
                               SUM(CASE WHEN e.validado = 1 AND LENGTH(TRIM(COALESCE(e.numero_recibo, ''))) > 0 THEN 1 ELSE 0 END) AS aceitos,
                               SUM(CASE WHEN e.i_resposta = 202 THEN 1 ELSE 0 END) AS com_advertencia,
                               SUM(CASE WHEN e.i_resposta IN (401, 411) THEN 1 ELSE 0 END) AS rejeitados,
                               SUM(CASE WHEN e.aguardando_ajuste = 1 THEN 1 ELSE 0 END) AS aguardando_ajuste,
                               MAX(e.data_criacao_registro) AS ultimo_envio
                          FROM {B}foesocial_dados_eventos e
                         WHERE e.codi_emp = ? AND e.i_evento_esocial IN (1200, 1210) AND e.competencia_calculo = ? GROUP BY e.i_evento_esocial ORDER BY e.i_evento_esocial""", (empresa, ini))
        pend = m._sql(f"""SELECT TOP 20 e.i_dados_eventos, e.i_evento_esocial, c.descricao AS evento, e.competencia_calculo, e.i_resposta, e.aguardando_ajuste,
                                 LEFT(COALESCE(e.descricao_resposta, ''), 160) AS resposta, e.data_criacao_registro
                            FROM {B}foesocial_dados_eventos e LEFT JOIN {B}foesocial_eventos c ON c.i_evento_esocial = e.i_evento_esocial
                           WHERE e.codi_emp = ? AND LENGTH(TRIM(COALESCE(e.numero_recibo, ''))) = 0 ORDER BY e.i_dados_eventos DESC""", (empresa,))
        npend = m._sql(f"SELECT COUNT(*) AS n FROM {B}foesocial_dados_eventos WHERE codi_emp = ? AND LENGTH(TRIM(COALESCE(numero_recibo, ''))) = 0", (empresa,))[0]["n"]
        total = m._sql(f"SELECT COUNT(*) AS n FROM {B}foesocial_dados_eventos WHERE codi_emp = ?", (empresa,))[0]["n"]
        if fech:
            f = fech[0]
            estado = ("fechada" if f["i_evento_esocial"] == 1299 else "reaberta")
            if estado == "fechada" and not (f["validado"] == 1 and (f["numero_recibo"] or "").strip()):
                estado = "fechamento_enviado_sem_aceite"
            fechamento = {"estado": estado, "ultimo_evento": "S-%d" % f["i_evento_esocial"], "envio": f["i_dados_eventos"], "recibo": (f["numero_recibo"] or "").strip() or None,
                          "em": f["data_criacao_registro"].isoformat() if f["data_criacao_registro"] else None}
        else:
            fechamento = {"estado": "sem_fechamento", "ultimo_evento": None}
        nome = {1200: "S-1200 Remuneração", 1210: "S-1210 Pagamentos"}
        r = {
            "empresa": empresa, "competencia": ini.isoformat()[:7],
            "fechamento_da_folha": fechamento,
            "eventos_da_competencia": [{"evento": nome[x["i_evento_esocial"]], "enviados": x["enviados"], "aceitos_com_recibo": x["aceitos"], "com_advertencia": x["com_advertencia"],
                                        "rejeitados": x["rejeitados"], "aguardando_ajuste": x["aguardando_ajuste"],
                                        "ultimo_envio": x["ultimo_envio"].isoformat() if x["ultimo_envio"] else None} for x in ev],
            "pendencias": {"eventos_sem_recibo_da_empresa": npend, "total_de_eventos_da_empresa": total,
                           "mais_recentes": [{"envio": x["i_dados_eventos"], "evento": f"S-{x['i_evento_esocial']} {(x['evento'] or '').strip()}",
                                              "competencia": x["competencia_calculo"].isoformat()[:7] if x["competencia_calculo"] else None, "resposta": x["i_resposta"],
                                              "aguardando_ajuste": x["aguardando_ajuste"] == 1, "mensagem": (x["resposta"] or "").strip() or None} for x in pend]},
        }
        avisos = []
        if fechamento["estado"] == "sem_fechamento":
            avisos.append("Não há S-1299 (nem S-1298) nesta competência: a empresa pode não usar o eSocial, ou a competência ainda não foi fechada.")
        if fechamento["estado"] == "reaberta":
            avisos.append("A competência foi reaberta (S-1298) e ainda não foi fechada de novo.")
        if any(x["rejeitados"] for x in r["eventos_da_competencia"]):
            avisos.append("Há eventos rejeitados (resposta 401/411) nesta competência.")
        if avisos:
            r["avisos"] = avisos
        return r

    return m._executar("situacao_esocial", {"empresa": empresa, "competencia": competencia}, run)


# ===================================================================================== memória de cálculo da folha
def memoria_calculo_folha(m: Motor, empresa: int, empregado: int, competencia: str, tipo_folha: int | None = None) -> dict:
    """Memória de cálculo da folha de um empregado numa competência: cada base de cálculo (INSS, FGTS, IRRF, férias, empréstimos...) com a base, a taxa e o valor.

    Lê as bases de focalculosbases dos cálculos (I_CALCULOS) do empregado em fobasesserv; só traz bases com valor ou base diferente de zero.
    Dados de remuneração por pessoa identificável: uso restrito (campo `sensivel: financeiro` no modelo)."""
    empresa, empregado = int(empresa), int(empregado)
    ini, _ = _mes(competencia)

    def run():
        sql = f"""SELECT s.tipo_process, s.i_servicos, s.rateio, s.proventos, s.descontos, c.i_cadbases, c.descricao AS base_nome,
                         b.base, b.taxa, b.valor, b.descricao_calculo,
                         (SELECT SUM(mv.valor_cal) FROM {B}fomovtoserv mv WHERE mv.codi_emp = s.codi_emp AND mv.i_calculos = s.i_calculos AND mv.prov_desc = 'P'
                             AND mv.i_eventos IN (SELECT eb.i_eventos FROM {B}foeventosbases eb WHERE eb.codi_emp = s.codi_emp AND eb.i_cadbases = c.i_cadbases)) AS soma_incidente
                    FROM {B}fobasesserv s
                    JOIN {B}focalculosbases b ON b.i_calculos = s.i_calculos
                    JOIN {B}focadbases c ON c.i_cadbases = b.i_cadbases
                   WHERE s.codi_emp = ? AND s.i_empregados = ? AND s.competencia = ? {"AND s.tipo_process = ?" if tipo_folha is not None else ""}
                     AND (b.base <> 0 OR b.valor <> 0)
                   ORDER BY s.tipo_process, s.i_servicos, s.rateio, c.i_cadbases"""
        par = (empresa, empregado, ini) + ((int(tipo_folha),) if tipo_folha is not None else ())
        rows = m._sql(sql, par)
        if not rows:
            raise ErroUso(f"Nenhuma base de cálculo para o empregado {empregado} da empresa {empresa} em {ini.isoformat()[:7]}"
                          + (f" (tipo de folha {tipo_folha})" if tipo_folha is not None else "") + ". Confira a competência, o código do empregado e o tipo de folha.")
        tipos = m.doms.get("tipo_folha", {}).get("valores", {})
        grupos: dict = {}
        for r in rows:
            k = (r["tipo_process"], r["i_servicos"], r["rateio"])
            g = grupos.setdefault(k, {"tipo_folha": {"codigo": r["tipo_process"], "significado": tipos.get(r["tipo_process"])}, "servico": r["i_servicos"], "rateio": r["rateio"],
                                      "proventos": _n(r["proventos"]), "descontos": _n(r["descontos"]), "bases": []})
            base, taxa, valor = _n(r["base"]), float(r["taxa"] or 0), _n(r["valor"])
            item = {"base_codigo": r["i_cadbases"], "base": (r["base_nome"] or "").strip(), "valor_da_base": base, "taxa": round(taxa, 4), "valor": valor}
            if (r["descricao_calculo"] or "").strip():
                item["como_foi_calculado"] = r["descricao_calculo"].strip()
            if taxa:
                item["valor_igual_base_x_taxa"] = abs(valor - round(base * taxa / 100, 2)) < 0.02
            if r["soma_incidente"] is not None:
                soma = _n(r["soma_incidente"])
                item["soma_dos_proventos_que_incidem"] = soma
                item["base_x_soma"] = "igual" if abs(base - soma) < 0.02 else "base menor (possível teto)" if base < soma else "base maior"
            g["bases"].append(item)
        out = list(grupos.values())
        return {"empresa": empresa, "empregado": empregado, "competencia": ini.isoformat()[:7], "calculos": out,
                "aviso": ("Cada cálculo é uma linha de fobasesserv (tipo de folha, serviço e rateio). `valor_igual_base_x_taxa` é falso nas bases progressivas "
                          "(INSS, IRRF) e nas com dedução (86,6% das bases com taxa seguiam valor = base x taxa / 100). `soma_dos_proventos_que_incidem` soma os proventos cujos "
                          "eventos incidem na base (foeventosbases): na base 9 (INSS mensal) a base gravada é igual a essa soma em 84,6% dos cálculos e fica no teto do INSS em outros 5%; "
                          "nas demais bases a comparação é só informativa.")}

    return m._executar("memoria_calculo_folha", {"empresa": empresa, "empregado": empregado, "competencia": competencia, "tipo_folha": tipo_folha}, run)


# ===================================================================================== guias de impostos do mês
def guias_do_mes(m: Motor, empresa: int, competencia: str, incluir_sem_saldo: bool = False) -> dict:
    """Guias de impostos da empresa numa competência: imposto, código de recolhimento, vencimento, saldo a recolher, valor pago e situação.

    ATENÇÃO: o registro de pagamentos no sistema está praticamente parado entre 2023 e 2025, conforme a empresa (guias de 2024 em diante quase nunca têm valor pago; o último pagamento gravado é de 2025-04): `sem_pagamento_registrado`
    NÃO significa guia em aberto. Onde há registro, o valor pago desta apuração fecha com a soma dos pagamentos em 98,2% das guias (2023-2024)."""
    empresa = int(empresa)
    ini, _ = _mes(competencia)

    def run():
        rows = m._sql(f"""SELECT r.codi_imp, g.nome_imp, g.sigl_imp, r.pdic_sim, r.i_recolhimento, r.codigo_recolhimento, r.parcela, r.data_vencimento,
                                 r.saldo_recolher, r.valor_pago, r.saldo_credor, r.saldo_credor_anterior
                            FROM {B}efsdoimp_por_recolhimento r LEFT JOIN {B}geimposto g ON g.codi_emp = r.codi_emp AND g.codi_imp = r.codi_imp
                           WHERE r.codi_emp = ? AND r.data_sim = ? {"" if incluir_sem_saldo else "AND r.saldo_recolher > 0"} ORDER BY r.codi_imp, r.i_recolhimento""", (empresa, ini))
        pags = m._sql(f"""SELECT codi_imp, pdic_pim, dpag_pim, vpag_pim, vjur_pim, vmul_pim, banco_pim FROM {B}efpagimp
                           WHERE codi_emp = ? AND data_pim = ? ORDER BY codi_imp, dpag_pim""", (empresa, ini))
        hoje = datetime.date.today()
        per = m.doms.get("periodicidade_guia", {}).get("valores", {})
        guias = []
        for x in rows:
            saldo, pago = _n(x["saldo_recolher"]), _n(x["valor_pago"])
            if saldo <= 0:
                sit = "sem_saldo_a_recolher"
            elif pago >= saldo - 0.01:
                sit = "paga"
            elif pago > 0:
                sit = "paga_parcialmente"
            elif x["data_vencimento"] and x["data_vencimento"] < hoje:
                sit = "vencida_sem_pagamento_registrado"
            else:
                sit = "a_vencer_sem_pagamento_registrado"
            guias.append({"imposto": {"codigo": x["codi_imp"], "nome": (x["nome_imp"] or "").strip(), "sigla": (x["sigl_imp"] or "").strip()},
                          "periodicidade": per.get(x["pdic_sim"], x["pdic_sim"]), "codigo_recolhimento": (x["codigo_recolhimento"] or "").strip(), "parcela": x["parcela"],
                          "vencimento": x["data_vencimento"].isoformat() if x["data_vencimento"] else None, "saldo_a_recolher": saldo, "valor_pago": pago,
                          "saldo_em_aberto": round(max(saldo - pago, 0), 2), "situacao": sit,
                          "saldo_credor": _n(x["saldo_credor"])})
        pagamentos = [{"imposto": p_["codi_imp"], "data": p_["dpag_pim"].isoformat() if p_["dpag_pim"] else None, "valor": _n(p_["vpag_pim"]),
                       "juros": _n(p_["vjur_pim"]), "multa": _n(p_["vmul_pim"]), "banco": p_["banco_pim"]} for p_ in pags]
        r = {"empresa": empresa, "competencia": ini.isoformat()[:7], "guias": guias, "pagamentos_registrados": pagamentos,
             "totais": {"saldo_a_recolher": round(sum(g["saldo_a_recolher"] for g in guias), 2), "valor_pago": round(sum(g["valor_pago"] for g in guias), 2),
                        "saldo_em_aberto": round(sum(g["saldo_em_aberto"] for g in guias), 2)}}
        avisos = []
        if ini >= datetime.date(2024, 1, 1):
            avisos.append("O registro de pagamentos de impostos no sistema é praticamente inexistente a partir de 2024 (efpagimp termina em 2025-04): 'sem pagamento registrado' não "
                          "significa guia em aberto. Confirme o pagamento no banco, no extrato ou nas obrigações acessórias.")
        if not rows:
            avisos.append("Nenhuma apuração por recolhimento nesta competência: a empresa pode não ter escrita fiscal, a apuração pode não ter sido calculada, ou não há saldo a recolher.")
        if avisos:
            r["avisos"] = avisos
        return r

    return m._executar("guias_do_mes", {"empresa": empresa, "competencia": competencia, "incluir_sem_saldo": incluir_sem_saldo}, run)


# ===================================================================================== perfil completo da empresa
def perfil_empresa(m: Motor, empresa: int, data: str | None = None) -> dict:
    """Perfil completo da empresa: cadastro, perfil fiscal (regimes e impostos), parâmetros da contabilidade e da folha, e situação do eSocial.

    Porta de entrada para entender uma empresa antes de consultar o resto: junta o que `perfil_fiscal` e `situacao_esocial` devolvem com o cadastro e os parâmetros
    contábeis e de folha. Cada bloco que a empresa não tem vem como null, com o motivo. Contém CNPJ/CPF (dado identificável)."""
    empresa = int(empresa)
    dia = _coagir(data) if data else datetime.date.today()
    if not isinstance(dia, datetime.date):
        raise ErroUso("data deve estar no formato AAAA-MM-DD.")

    def run():
        e = m._sql(f"""SELECT codi_emp, nome_emp, cgce_emp, tins_emp, stat_emp, uefi_emp, ucta_emp, ufol_emp, upto_emp, uhon_emp, upat_emp
                         FROM {B}geempre WHERE codi_emp = ?""", (empresa,))
        if not e:
            raise ErroUso(f"Empresa {empresa} não existe no cadastro.")
        e = e[0]
        doc = (e["cgce_emp"] or "").strip()
        status = m.doms.get("status_empresa", {}).get("valores", {})
        r = {"empresa": empresa, "data": dia.isoformat(),
             "cadastro": {"nome": (e["nome_emp"] or "").strip(), "documento": doc, "tipo_documento": "CNPJ" if len(doc) == 14 else "CPF" if len(doc) == 11 else None,
                          "situacao": {"codigo": e["stat_emp"], "significado": status.get(e["stat_emp"])},
                          "usa_modulos": {"escrita_fiscal": e["uefi_emp"] == 1, "contabilidade": e["ucta_emp"] == 1, "folha": e["ufol_emp"] == 1, "ponto": e["upto_emp"] == 1,
                                          "honorarios": e["uhon_emp"] == 1, "patrimonio": e["upat_emp"] == 1}}}
        try:
            fiscal = perfil_fiscal(m, empresa, dia.isoformat())
            r["fiscal"] = {k: fiscal[k] for k in ("vigencia_em_uso", "regime_federal", "regime_estadual", "regime_municipal", "gera_lancamentos_contabeis", "impostos_ativos", "evidencias_12_meses") if k in fiscal}
            if "avisos" in fiscal:
                r["fiscal"]["avisos"] = fiscal["avisos"]
        except ErroUso as ex:
            r["fiscal"] = None
            r.setdefault("observacoes", []).append(f"Fiscal: {ex}")
        g = m._sql(f"SELECT peri_par, pfec_par, sped_fiscal_par, esto_par, gera_lancamentos_par FROM {B}efparametro WHERE codi_emp = ?", (empresa,))
        if g and r.get("fiscal") is not None:
            g = g[0]
            r["fiscal"]["escrita_fiscal"] = {"periodo_atual": g["peri_par"].isoformat()[:7] if g["peri_par"] else None,
                                             "fechamento_fiscal": g["pfec_par"].isoformat() if g["pfec_par"] else None,
                                             "gera_sped_fiscal": g["sped_fiscal_par"] == "S", "controla_estoque": g["esto_par"] == 1}
            if g["pfec_par"] and g["peri_par"] and g["pfec_par"] < g["peri_par"]:
                r["fiscal"].setdefault("avisos", []).append("O fechamento fiscal (data após a qual não se lança) está anterior ao período atual de trabalho; é comum (1.433 das 1.434 empresas).")
        c = m._sql(f"""SELECT ctcx_par, masc_par, codi_pad, comp_pad, dini_par, dfin_par, lant_par, ccusto_par, dre_par, dila_par FROM {B}ctparmto WHERE codi_emp = ?""", (empresa,))
        if c:
            c = c[0]
            r["contabilidade"] = {"regime": m.doms.get("regime_contabil", {}).get("valores", {}).get(c["ctcx_par"], c["ctcx_par"]), "mascara_plano_contas": (c["masc_par"] or "").strip(),
                                  "plano_de_contas_da_empresa": c["codi_pad"] if c["codi_pad"] else empresa, "plano_proprio": not c["codi_pad"],
                                  "inicio_dos_lancamentos": c["dila_par"].isoformat() if c["dila_par"] else None,
                                  "periodo_de_trabalho": {"inicio": c["dini_par"].isoformat() if c["dini_par"] else None, "fim": c["dfin_par"].isoformat() if c["dfin_par"] else None,
                                                          "fora_do_periodo": m.doms.get("acao_periodo_trabalho", {}).get("valores", {}).get(c["lant_par"], c["lant_par"])},
                                  "por_centro_de_custo": c["ccusto_par"] == "S", "usa_dre": c["dre_par"] == "S"}
        else:
            r["contabilidade"] = None
            r.setdefault("observacoes", []).append("Contabilidade: sem parâmetros (empresa não usa o módulo contábil).")
        f = m._sql(f"""SELECT data_proces, tipo_proces, cta_gera, usa_rateio, adiant_percentual, data_pagto_mes FROM {B}foparmto WHERE codi_emp = ?""", (empresa,))
        if f:
            f = f[0]
            r["folha"] = {"competencia_atual": f["data_proces"].isoformat()[:7] if f["data_proces"] else None,
                          "tipo_folha_atual": m.doms.get("tipo_folha_atual", {}).get("valores", {}).get(f["tipo_proces"], f["tipo_proces"]), "gera_lancamentos_contabeis": f["cta_gera"] == 1,
                          "usa_rateio_por_servico": f["usa_rateio"] == 1, "percentual_adiantamento": float(f["adiant_percentual"] or 0)}
            n = m._sql(f"SELECT COUNT(DISTINCT i_empregados) AS n FROM {B}foempregados WHERE codi_emp = ?", (empresa,))[0]["n"]
            r["folha"]["empregados_cadastrados"] = n
        else:
            r["folha"] = None
            r.setdefault("observacoes", []).append("Folha: sem parâmetros (empresa não usa o módulo de folha).")
        ult = m._sql(f"""SELECT TOP 1 competencia_calculo, i_evento_esocial, numero_recibo FROM {B}foesocial_dados_eventos
                          WHERE codi_emp = ? AND i_evento_esocial IN (1298, 1299) ORDER BY i_dados_eventos DESC""", (empresa,))
        if ult:
            u = ult[0]
            r["esocial"] = {"ultimo_evento_de_fechamento": f"S-{u['i_evento_esocial']}", "competencia": u["competencia_calculo"].isoformat()[:7] if u["competencia_calculo"] else None,
                            "com_recibo": bool((u["numero_recibo"] or "").strip()), "detalhe": "use situacao_esocial(empresa, competencia)"}
        else:
            r["esocial"] = None
        return r

    return m._executar("perfil_empresa", {"empresa": empresa, "data": data}, run)


# ===================================================================================== informativos (obrigações acessórias) da empresa
def informativos_da_empresa(m: Motor, empresa: int, de: str, ate: str | None = None, informativo: int | None = None) -> dict:
    """Informativos (obrigações acessórias) preparados para a empresa no período: qual obrigação, competência, nº de campos informados, retificadora e número de recibo.

    Vem de efoutrosdados/efoutrosdados_dados ("outros dados" de cada obrigação). Informativos anuais (DEFIS, DIRF, DMED) têm competência = 1º de janeiro do ano.
    `numero_recibo` e `retificadora` só existem em alguns informativos (DCTF, DIRF, Reinf...): vazio não prova que a obrigação não foi transmitida."""
    empresa = int(empresa)
    d1, _ = _mes(de)
    d2 = _mes(ate)[0] if ate else d1
    if d2 < d1:
        raise ErroUso("ate deve ser maior ou igual a de.")

    def run():
        sql = f"""SELECT h.competencia, h.i_informativos, i.descricao,
                         (SELECT COUNT(*) FROM {B}efoutrosdados_dados d WHERE d.codi_emp = h.codi_emp AND d.competencia = h.competencia AND d.i_informativos = h.i_informativos) AS campos,
                         (SELECT MAX(d.valor) FROM {B}efoutrosdados_dados d WHERE d.codi_emp = h.codi_emp AND d.competencia = h.competencia AND d.i_informativos = h.i_informativos AND d.campo = 'numero_recibo') AS recibo,
                         (SELECT MAX(d.valor) FROM {B}efoutrosdados_dados d WHERE d.codi_emp = h.codi_emp AND d.competencia = h.competencia AND d.i_informativos = h.i_informativos AND d.campo = 'retificadora') AS retificadora
                    FROM {B}efoutrosdados h JOIN {B}efinformativos i ON i.i_informativos = h.i_informativos
                   WHERE h.codi_emp = ? AND h.competencia >= ? AND h.competencia <= ? {"AND h.i_informativos = ?" if informativo is not None else ""}
                   ORDER BY h.competencia DESC, h.i_informativos"""
        par = (empresa, d1, d2) + ((int(informativo),) if informativo is not None else ())
        rows = m._sql(sql, par)
        itens = [{"competencia": x["competencia"].isoformat()[:7], "informativo": {"codigo": x["i_informativos"], "nome": (x["descricao"] or "").strip()}, "campos_informados": x["campos"],
                  "numero_recibo": (x["recibo"] or "").strip() or None, "retificadora": ((x["retificadora"] or "").strip() or None)} for x in rows]
        por = {}
        for it in itens:
            por.setdefault(it["informativo"]["nome"], 0)
            por[it["informativo"]["nome"]] += 1
        r = {"empresa": empresa, "periodo": [d1.isoformat()[:7], d2.isoformat()[:7]], "total": len(itens), "por_informativo": por, "informativos": itens}
        if not itens:
            r["aviso"] = "Nenhum informativo preparado neste período: a obrigação pode não ter sido gerada pelo sistema, ou a empresa não está sujeita a ela."
        return r

    return m._executar("informativos_da_empresa", {"empresa": empresa, "de": de, "ate": ate, "informativo": informativo}, run)


# ===================================================================================== apuração do Lalur (lucro real)
def apuracao_lalur(m: Motor, empresa: int, competencia: str) -> dict:
    """Apuração do IRPJ e da CSLL pelo lucro real (Lalur) da empresa numa competência, com a conferência das identidades do cálculo.

    Usa o cálculo mais recente da competência (a empresa pode recalcular). Traz o IRPJ (lucro real, 15%, adicional, deduções, a recolher) e a CSLL (base, 9%, deduções,
    a recolher), e `conferencia`: recalcula cada passo e diz se bate com o gravado (validado em 3.108 cálculos: lucro real, base, 15%, 9%, adicional e a recolher com piso zero)."""
    empresa = int(empresa)
    ini, _ = _mes(competencia)

    def run():
        cab = m._sql(f"SELECT TOP 1 i_calculo, usuario, data_hora FROM {B}lrcalculo WHERE codi_emp = ? AND competencia = ? ORDER BY i_calculo DESC", (empresa, ini))
        if not cab:
            raise ErroUso(f"Não há cálculo do Lalur para a empresa {empresa} em {ini.isoformat()[:7]} (a empresa pode não ser do lucro real, ou o cálculo não foi feito).")
        calc = cab[0]["i_calculo"]
        irpj = m._sql(f"SELECT * FROM {B}lrcalculo_irpj_real WHERE codi_emp = ? AND i_calculo = ? ORDER BY ajuste_anual", (empresa, calc))
        csll = m._sql(f"SELECT * FROM {B}lrcalculo_csll_real WHERE codi_emp = ? AND i_calculo = ? ORDER BY ajuste_anual", (empresa, calc))
        antes = m._sql(f"SELECT TOP 1 valor_lucro_operacional, valor_prejuizo_operacional, valor_lucro_nao_operacional, valor_prejuizo_nao_operacional "
                       f"FROM {B}lrlucro_antes_csll_irpj WHERE codi_emp = ? AND competencia = ? ORDER BY i_lucro_antes DESC", (empresa, ini))

        def f(x, k):
            return _n(x.get(k))
        conf = []

        def teste(nome, esperado, gravado, tol=0.02):
            conf.append({"verificacao": nome, "recalculado": round(esperado, 2), "gravado": round(gravado, 2), "confere": abs(esperado - gravado) < tol})
        ded_irpj = ["valor_deducao_pago_em_mes_anterior", "valor_deducao_irrf", "valor_deducao_orgao_publico_federal", "valor_deducao_administracao_publica",
                    "valor_deducao_outra_deducao", "valor_deducao_pago_exterior", "valor_deducao_pago_incidente_sobre_ganhos", "valor_deducao_parcelamento_formalizado",
                    "valor_deducao_compensacao_imposto_federal_periodo_anterior", "valor_deducao_saldo_periodo_anterior"]
        out_irpj = []
        for x in irpj:
            tag = "IRPJ (ajuste anual)" if x["ajuste_anual"] == 1 else "IRPJ"
            teste(f"{tag}: lucro real antes da compensação = lucro líquido + adições − exclusões",
                  f(x, "valor_lucro_liquido_antes_irpj") + f(x, "valor_adicao") - f(x, "valor_exclusao"), f(x, "valor_lucro_real_antes_compensacao"))
            teste(f"{tag}: lucro real = antes da compensação − compensação", f(x, "valor_lucro_real_antes_compensacao") - f(x, "valor_compensacao"), f(x, "valor_lucro_real"))
            teste(f"{tag}: IRPJ devido = 15% do lucro real positivo", round(max(f(x, "valor_lucro_real"), 0) * 0.15, 2), f(x, "valor_irpj_devido"))
            if f(x, "valor_adicional") > 0:
                meses = (f(x, "valor_lucro_real") - f(x, "valor_adicional") * 10) / 20000
                conf.append({"verificacao": f"{tag}: adicional = 10% × (lucro real − 20.000 × meses)", "meses_implicitos": round(meses, 4),
                             "confere": abs(meses - round(meses)) < 0.001 and 1 <= round(meses) <= 12})
            teste(f"{tag}: deduções = soma das parcelas", sum(f(x, k) for k in ded_irpj), f(x, "valor_deducao"))
            bruto = (f(x, "valor_irpj_devido") + f(x, "valor_adicional") - f(x, "valor_deducao") - f(x, "valor_incentivo_fiscal") - f(x, "valor_reducao_lucro_exploracao")
                     - f(x, "valor_reducao_por_reinvestimento") + f(x, "valor_diferido_periodo_anterior") - f(x, "valor_diferido_periodo"))
            teste(f"{tag}: a recolher = max(0, devido + adicional − deduções − incentivos − reduções + diferido anterior − diferido)", max(bruto, 0), f(x, "valor_a_recolher"))
            out_irpj.append({"ajuste_anual": x["ajuste_anual"] == 1, "lucro_liquido_antes_irpj": f(x, "valor_lucro_liquido_antes_irpj"), "adicoes": f(x, "valor_adicao"),
                             "exclusoes": f(x, "valor_exclusao"), "compensacao": f(x, "valor_compensacao"), "lucro_real": f(x, "valor_lucro_real"),
                             "irpj_devido": f(x, "valor_irpj_devido"), "adicional": f(x, "valor_adicional"), "deducoes": f(x, "valor_deducao"),
                             "incentivos": f(x, "valor_incentivo_fiscal"), "a_recolher": f(x, "valor_a_recolher"),
                             "compensar_periodo_seguinte": f(x, "valor_compensar_periodo_seguinte")})
        out_csll = []
        for x in csll:
            tag = "CSLL (ajuste anual)" if x["ajuste_anual"] == 1 else "CSLL"
            teste(f"{tag}: base antes da compensação = lucro + adições − exclusões",
                  f(x, "valor_lucro_liquido_antes_csll_irpj") + f(x, "valor_adicao") - f(x, "valor_exclusao"), f(x, "valor_base_calculo_antes_compensacao"))
            teste(f"{tag}: base = antes da compensação − compensação", f(x, "valor_base_calculo_antes_compensacao") - f(x, "valor_compensacao"), f(x, "valor_base_calculo"))
            teste(f"{tag}: CSLL devida = 9% da base positiva", round(max(f(x, "valor_base_calculo"), 0) * 0.09, 2), f(x, "valor_csll_devida"), tol=0.05)
            bruto = (f(x, "valor_csll_devida") - f(x, "valor_deducao") - f(x, "valor_isencao_prouni") - f(x, "valor_bonus_adimplencia")
                     + f(x, "valor_diferido_periodo_anterior") - f(x, "valor_diferido_periodo"))
            teste(f"{tag}: a recolher = max(0, devida − deduções − Prouni − bônus + diferido anterior − diferido)", max(bruto, 0), f(x, "valor_a_recolher"))
            out_csll.append({"ajuste_anual": x["ajuste_anual"] == 1, "base_calculo": f(x, "valor_base_calculo"), "csll_devida": f(x, "valor_csll_devida"),
                             "deducoes": f(x, "valor_deducao"), "a_recolher": f(x, "valor_a_recolher"),
                             "compensar_periodo_seguinte": f(x, "valor_compensar_periodo_seguinte")})
        r = {"empresa": empresa, "competencia": ini.isoformat()[:7],
             "calculo": {"codigo": calc, "usuario": (cab[0]["usuario"] or "").strip(), "em": cab[0]["data_hora"].isoformat() if cab[0]["data_hora"] else None},
             "irpj": out_irpj, "csll": out_csll, "conferencia": conf, "tudo_confere": all(c["confere"] for c in conf)}
        if antes:
            a = antes[0]
            r["lucro_antes_irpj_csll"] = {"lucro_operacional": _n(a["valor_lucro_operacional"]), "prejuizo_operacional": _n(a["valor_prejuizo_operacional"]),
                                          "lucro_nao_operacional": _n(a["valor_lucro_nao_operacional"]), "prejuizo_nao_operacional": _n(a["valor_prejuizo_nao_operacional"])}
        if not r["tudo_confere"]:
            r["aviso"] = "Alguma verificação não bate: pode haver ajuste manual, regra específica (rural, SCP, cisão) ou caso ainda não visto. Veja `conferencia`."
        return r

    return m._executar("apuracao_lalur", {"empresa": empresa, "competencia": competencia}, run)


# ===================================================================================== situação do DAS / PGDAS-D por API
def situacao_das(m: Motor, empresa: int, competencia: str) -> dict:
    """Situação do DAS (Simples Nacional) da empresa numa competência: apuração, declaração PGDAS-D transmitida pela API, guia DAS emitida e erros recentes.

    Estado: sem_apuracao | declaracao_nao_transmitida | declarada_sem_das | declarada_e_das_emitido. A integração por API só existe a partir de 2024-04: antes disso
    o estado não pode ser deduzido. Retificadora = declaração transmitida com sucesso depois da primeira na mesma competência (por evidência: 1.334 de 1.334)."""
    empresa = int(empresa)
    ini, _ = _mes(competencia)

    def run():
        ap = m._sql(f"""SELECT SUM(CASE WHEN anexo = 0 THEN basen ELSE 0 END) AS base, SUM(CASE WHEN anexo = 0 THEN valorn ELSE 0 END) AS imposto, COUNT(*) AS linhas
                          FROM {B}efsdoimp_simples_nacional WHERE codi_emp = ? AND codi_imp = 44 AND data_sim = ?""", (empresa, ini))[0]
        envios = m._sql(f"""SELECT i_envio, tipo_envio, situacao, tipo_declaracao, data_envio, horario_envio, numero_das, valor_diferente_sistema
                              FROM {B}efdas_api_envio_arquivos WHERE codi_emp = ? AND competencia = ? ORDER BY i_envio""", (empresa, ini))
        decl = [e for e in envios if e["tipo_envio"] == 1 and e["situacao"] == 1]
        das = [e for e in envios if e["tipo_envio"] == 2 and e["situacao"] == 1 and (e["numero_das"] or "").strip()]
        falhas = [e for e in envios if e["situacao"] in (2, 3, 4)]
        msgs = {}
        if falhas:
            ids = [f["i_envio"] for f in falhas[-3:]]
            for x in m._sql(f"""SELECT i_envio, codigo_mensagem, titulo_mensagem, LEFT(COALESCE(descricao_mensagem, ''), 240) AS descricao FROM {B}efdas_api_envio_arquivos_mensagem
                                 WHERE codi_emp = ? AND i_envio IN ({','.join(str(i) for i in ids)}) ORDER BY i_envio, sequencial_mensagem""", (empresa,)):
                msgs.setdefault(x["i_envio"], []).append({"codigo": x["codigo_mensagem"], "titulo": (x["titulo_mensagem"] or "").strip(), "descricao": (x["descricao"] or "").strip()})
        tem_ap = bool(ap["linhas"])
        if not tem_ap:
            estado = "sem_apuracao"
        elif not decl:
            estado = "declaracao_nao_transmitida"
        elif not das:
            estado = "declarada_sem_das"
        else:
            estado = "declarada_e_das_emitido"

        def quando(e):
            return f"{e['data_envio'].isoformat()} {str(e['horario_envio'])[:8]}" if e["data_envio"] else None
        r = {"empresa": empresa, "competencia": ini.isoformat()[:7], "estado": estado,
             "apuracao_simples": ({"base_calculo": _n(ap["base"]), "imposto": _n(ap["imposto"]), "sem_movimento": _n(ap["base"]) == 0} if tem_ap else None),
             "declaracao": ({"transmissoes_com_sucesso": len(decl), "retificadoras": sum(1 for e in decl[1:] if e["tipo_declaracao"] == 2),
                             "ultima": {"envio": decl[-1]["i_envio"], "em": quando(decl[-1]), "tipo": "retificadora" if decl[-1]["tipo_declaracao"] == 2 else "original"}} if decl else None),
             "guia_das": ({"numero": das[-1]["numero_das"].strip(), "emitida_em": quando(das[-1]), "emissoes_com_numero": len(das),
                           "valor_diferente_do_sistema": {"S": True, "N": False}.get((das[-1]["valor_diferente_sistema"] or "").strip())} if das else None),
             "erros_recentes": [{"envio": f["i_envio"], "em": quando(f), "situacao": {2: "recusado pela API", 3: "erro no servidor", 4: "não autorizado"}[f["situacao"]],
                                 "mensagens": msgs.get(f["i_envio"], [])} for f in falhas[-3:]],
             "total_de_envios": len(envios)}
        avisos = []
        if ini < datetime.date(2024, 4, 1):
            avisos.append("A integração por API só registra envios a partir de 2024-04: para esta competência o estado não pode ser deduzido destas tabelas.")
        sem_mov = bool(tem_ap) and _n(ap["base"]) == 0
        if estado == "declarada_sem_das" and not sem_mov:
            avisos.append("ATENÇÃO: há receita apurada e declaração transmitida, mas nenhuma emissão de guia com número: a guia pode ter sido emitida fora do sistema ou ter falhado (veja erros_recentes).")
        if estado == "declarada_sem_das" and sem_mov:
            avisos.append("Sem movimento (base zero): declaração transmitida e nenhuma guia a emitir — situação esperada.")
        if estado == "declaracao_nao_transmitida" and not sem_mov:
            avisos.append("ATENÇÃO: há receita apurada e nenhuma declaração PGDAS-D transmitida com sucesso por esta integração (pode ter sido feita pelo portal).")
        if estado == "sem_apuracao" and envios:
            avisos.append("Há envios à API sem apuração do Simples no sistema nesta competência.")
        if avisos:
            r["avisos"] = avisos
        return r

    return m._executar("situacao_das", {"empresa": empresa, "competencia": competencia}, run)


# ===================================================================================== receita bruta mensal (série)
def receita_bruta_mensal(m: Motor, empresa: int, de: str, ate: str) -> dict:
    """Receita bruta mês a mês (até 36 meses): saídas + serviços + cupons fiscais (CF-e) de acumuladores que incidem sobre receita bruta, menos devoluções de venda.

    Mesma regra de `receita_bruta_simples` (IREC_ACU/IDEV_ACU com a vigência do acumulador na data do documento), em série e sem exigir regime do Simples: serve para
    presumido, real e Simples. Para o Simples, cada mês traz também a base que a Domínio apurou, para comparação. Regime de competência (data do documento)."""
    empresa = int(empresa)
    d1, _ = _mes(de)
    d2, fim = _mes(ate)
    if d2 < d1:
        raise ErroUso("ate deve ser maior ou igual a de.")
    if (d2.year - d1.year) * 12 + d2.month - d1.month >= 36:
        raise ErroUso("O período máximo é de 36 meses.")

    def run():
        ini = d1
        sai = m._sql(f"""SELECT DATEFORMAT(n.dsai_sai, 'YYYY-MM') AS mes, COALESCE(SUM(CASE WHEN a.irec_acu = 'S' THEN n.vcon_sai ELSE 0 END), 0) AS v, COUNT(*) AS docs
                           FROM {B}efsaidas n LEFT JOIN {B}efacumulador_vigencia a ON a.codi_emp = n.codi_emp AND a.codi_acu = n.codi_acu AND {_vigencia('n', 'n.dsai_sai')}
                          WHERE n.codi_emp = ? AND n.cancelada_sai = 'N' AND n.dsai_sai >= ? AND n.dsai_sai < ? GROUP BY mes""", (empresa, ini, fim))
        ser = m._sql(f"""SELECT DATEFORMAT(n.dser_ser, 'YYYY-MM') AS mes, COALESCE(SUM(CASE WHEN a.irec_acu = 'S' THEN n.vcon_ser ELSE 0 END), 0) AS v, COUNT(*) AS docs
                           FROM {B}efservicos n LEFT JOIN {B}efacumulador_vigencia a ON a.codi_emp = n.codi_emp AND a.codi_acu = n.codi_acu AND {_vigencia('n', 'n.dser_ser')}
                          WHERE n.codi_emp = ? AND n.cancelada_ser = 'N' AND n.dser_ser >= ? AND n.dser_ser < ? GROUP BY mes""", (empresa, ini, fim))
        cfe = m._sql(f"""SELECT DATEFORMAT(h.data_cfe, 'YYYY-MM') AS mes, COALESCE(SUM(CASE WHEN a.irec_acu = 'S' THEN i.valor_total ELSE 0 END), 0) AS v, COUNT(DISTINCT h.i_cfe) AS docs
                           FROM {B}efcupom_fiscal_eletronico_impostos i JOIN {B}efcupom_fiscal_eletronico h ON h.codi_emp = i.codi_emp AND h.i_cfe = i.i_cfe
                           LEFT JOIN {B}efacumulador_vigencia a ON a.codi_emp = i.codi_emp AND a.codi_acu = i.codi_acu
                                AND a.vigencia_acu = (SELECT MAX(x.vigencia_acu) FROM {B}efacumulador_vigencia x WHERE x.codi_emp = i.codi_emp AND x.codi_acu = i.codi_acu AND x.vigencia_acu <= h.data_cfe)
                          WHERE i.codi_emp = ? AND h.situacao = 0 AND h.data_cfe >= ? AND h.data_cfe < ? GROUP BY mes""", (empresa, ini, fim))
        dev = m._sql(f"""SELECT DATEFORMAT(n.dent_ent, 'YYYY-MM') AS mes, COALESCE(SUM(CASE WHEN a.idev_acu = 'S' THEN n.vcon_ent ELSE 0 END), 0) AS v
                           FROM {B}efentradas n LEFT JOIN {B}efacumulador_vigencia a ON a.codi_emp = n.codi_emp AND a.codi_acu = n.codi_acu AND {_vigencia('n', 'n.dent_ent')}
                          WHERE n.codi_emp = ? AND n.dent_ent >= ? AND n.dent_ent < ? GROUP BY mes""", (empresa, ini, fim))
        simples = m._sql(f"""SELECT DATEFORMAT(data_sim, 'YYYY-MM') AS mes, SUM(basen) AS base FROM {B}efsdoimp_simples_nacional
                              WHERE codi_emp = ? AND codi_imp = 44 AND anexo = 0 AND data_sim >= ? AND data_sim < ? GROUP BY mes""", (empresa, ini, fim))
        idx = lambda rows: {x["mes"]: x for x in rows}
        S, V, C, D, P = idx(sai), idx(ser), idx(cfe), idx(dev), idx(simples)
        meses, y, mo = [], d1.year, d1.month
        while (y, mo) <= (d2.year, d2.month):
            meses.append(f"{y:04d}-{mo:02d}")
            mo += 1
            if mo == 13:
                y, mo = y + 1, 1
        linhas, tot = [], 0.0
        for k in meses:
            vs, vv, vc, vd = _n((S.get(k) or {}).get("v")), _n((V.get(k) or {}).get("v")), _n((C.get(k) or {}).get("v")), _n((D.get(k) or {}).get("v"))
            rb = round(vs + vv + vc - vd, 2)
            tot += rb
            linha = {"mes": k, "saidas": vs, "servicos": vv, "cupons_fiscais": vc, "devolucoes": vd, "receita_bruta": rb}
            if k in P:
                base = _n(P[k]["base"])
                linha["base_simples_apurada"] = base
                linha["diferenca_para_simples"] = round(rb - base, 2)
            linhas.append(linha)
        return {"empresa": empresa, "periodo": [meses[0], meses[-1]], "meses": linhas, "total_receita_bruta": round(tot, 2),
                "aviso": "Regime de competência (data do documento). Para empresas em regime de caixa a base apurada pode diferir. Acumuladores sem 'incide sobre receita bruta' não entram."}

    return m._executar("receita_bruta_mensal", {"empresa": empresa, "de": de, "ate": ate}, run)


# ===================================================================================== situação da EFD-Reinf
def situacao_reinf(m: Motor, empresa: int, competencia: str) -> dict:
    """Situação da EFD-Reinf da empresa numa competência: fechamento da série R-2000 (R-2099 / reabertura R-2098), eventos enviados por tipo e rejeições.

    Aceito = situação 1 com número de recibo (99,7% das situações 1 têm recibo); rejeitado = situação 3 (99,8% têm erro registrado); 0 = aguardando retorno.
    Eventos marcados como excluídos (R-9000) ficam fora. O fechamento vale o ÚLTIMO R-2098/R-2099 aceito da competência."""
    empresa = int(empresa)
    ini, _ = _mes(competencia)
    nomes = m.doms.get("evento_reinf", {}).get("valores", {})

    def run():
        ev = m._sql(f"""SELECT i_evento, COUNT(*) AS enviados, SUM(CASE WHEN situacao = 1 AND LENGTH(TRIM(COALESCE(numero_recibo, ''))) > 0 THEN 1 ELSE 0 END) AS aceitos,
                               SUM(CASE WHEN situacao = 3 THEN 1 ELSE 0 END) AS rejeitados, SUM(CASE WHEN situacao = 0 THEN 1 ELSE 0 END) AS aguardando,
                               MAX(data_envio) AS ultimo_envio
                          FROM {B}efd_reinf_envio_arquivos WHERE codi_emp = ? AND competencia = ? AND COALESCE(evento_excluido, 'N') <> 'S' AND i_evento <> 9000
                         GROUP BY i_evento ORDER BY i_evento""", (empresa, ini))
        fech = m._sql(f"""SELECT TOP 1 i_envio, i_evento, numero_recibo, data_envio FROM {B}efd_reinf_envio_arquivos
                           WHERE codi_emp = ? AND competencia = ? AND i_evento IN (2098, 2099) AND situacao = 1 AND COALESCE(evento_excluido, 'N') <> 'S' ORDER BY i_envio DESC""", (empresa, ini))
        fech4 = m._sql(f"""SELECT TOP 1 i_envio, tipo_envio, numero_recibo, data_envio FROM {B}efd_reinf_envio_arquivos
                            WHERE codi_emp = ? AND competencia = ? AND i_evento = 4099 AND situacao = 1 AND COALESCE(evento_excluido, 'N') <> 'S' ORDER BY i_envio DESC""", (empresa, ini))
        rej = m._sql(f"""SELECT TOP 5 e.i_envio, e.i_evento, er.codigo_erro, LEFT(COALESCE(er.mensagem_erro, ''), 200) AS mensagem
                           FROM {B}efd_reinf_envio_arquivos e LEFT JOIN {B}efd_reinf_envio_arquivos_erros er ON er.codi_emp = e.codi_emp AND er.i_envio = e.i_envio AND er.i_filial = e.i_filial
                          WHERE e.codi_emp = ? AND e.competencia = ? AND e.situacao = 3 AND COALESCE(e.evento_excluido, 'N') <> 'S' ORDER BY e.i_envio DESC""", (empresa, ini))

        def quando(x):
            return x.isoformat() if x else None
        if fech:
            f = fech[0]
            fechamento = {"estado": "fechada" if f["i_evento"] == 2099 else "reaberta", "ultimo_evento": f"R-{f['i_evento']}", "envio": f["i_envio"],
                          "recibo": (f["numero_recibo"] or "").strip() or None, "em": quando(f["data_envio"])}
        else:
            fechamento = {"estado": "sem_fechamento", "ultimo_evento": None}
        if fech4:
            f4 = fech4[0]
            fechamento4 = {"estado": "reaberta" if (f4["tipo_envio"] or "").strip() == "B" else "fechada", "tipo_do_ultimo_envio": (f4["tipo_envio"] or "").strip(), "envio": f4["i_envio"],
                           "recibo": (f4["numero_recibo"] or "").strip() or None, "em": quando(f4["data_envio"])}
        else:
            fechamento4 = None
        r = {"empresa": empresa, "competencia": ini.isoformat()[:7], "fechamento_serie_2000": fechamento, "fechamento_serie_4000": fechamento4,
             "eventos": [{"evento": nomes.get(x["i_evento"], f"R-{x['i_evento']}"), "enviados": x["enviados"], "aceitos": x["aceitos"], "rejeitados": x["rejeitados"],
                          "aguardando_retorno": x["aguardando"], "ultimo_envio": quando(x["ultimo_envio"])} for x in ev],
             "rejeicoes_recentes": [{"envio": x["i_envio"], "evento": f"R-{x['i_evento']}", "codigo_erro": x["codigo_erro"], "mensagem": (x["mensagem"] or "").strip() or None} for x in rej]}
        avisos = []
        if fechamento["estado"] == "sem_fechamento":
            avisos.append("Não há R-2099 (nem R-2098) aceito nesta competência: a empresa pode não usar a EFD-Reinf, não ter feito o fechamento, ou ele foi rejeitado.")
        if fechamento["estado"] == "reaberta":
            avisos.append("A competência foi reaberta (R-2098) e ainda não foi fechada de novo.")
        if rej:
            avisos.append("Há eventos rejeitados (situação 3) nesta competência.")
        if avisos:
            r["avisos"] = avisos
        return r

    return m._executar("situacao_reinf", {"empresa": empresa, "competencia": competencia}, run)


# ===================================================================================== resumo da folha de pagamento
def resumo_folha(m: Motor, empresa: int, competencia: str) -> dict:
    """Totais da folha da empresa numa competência, por tipo de folha: empregados, proventos, descontos e líquido (só agregados, sem identificar empregados).

    O líquido gravado (`foliquidosfilepr`) é igual a proventos − descontos em 254 de 254 cálculos/empregados conferidos (empresa 354, 2025+). Só a linha principal do cálculo (`rateio = 0`) entra: a Domínio grava também uma linha de rateio por serviço (`rateio = 1`) que REPETE os mesmos valores, e somar as duas dobra
    proventos e descontos. Nem toda base tem líquido
    gravado: os tipos 60, 61 e 92 nunca têm e parte da folha mensal também não — por isso há `liquido_gravado` e `bases_sem_liquido`. Dado financeiro da empresa."""
    empresa = int(empresa)
    ini, _ = _mes(competencia)

    def run():
        base = m._sql(f"""SELECT tipo_process, COUNT(DISTINCT i_empregados) AS empregados, COUNT(*) AS linhas, SUM(proventos) AS proventos, SUM(descontos) AS descontos
                            FROM {B}fobasesserv WHERE codi_emp = ? AND competencia = ? AND rateio = 0 GROUP BY tipo_process ORDER BY tipo_process""", (empresa, ini))
        if not base:
            raise ErroUso(f"Nenhuma folha da empresa {empresa} em {ini.isoformat()[:7]} (a empresa pode não usar a folha ou não ter calculado a competência).")
        liq = {x["tipo_process"]: x for x in m._sql(f"""SELECT b.tipo_process, SUM(l.liq) AS liquido, COUNT(*) AS pares
                                                         FROM (SELECT DISTINCT tipo_process, i_calculos, i_empregados FROM {B}fobasesserv WHERE codi_emp = ? AND competencia = ? AND rateio = 0) b
                                                         JOIN (SELECT i_calculos, i_empregados, SUM(liquido) AS liq FROM {B}foliquidosfilepr WHERE codi_emp = ? GROUP BY i_calculos, i_empregados) l
                                                           ON l.i_calculos = b.i_calculos AND l.i_empregados = b.i_empregados GROUP BY b.tipo_process""", (empresa, ini, empresa))}
        pares = {x["tipo_process"]: x["n"] for x in m._sql(f"SELECT tipo_process, COUNT(*) AS n FROM (SELECT DISTINCT tipo_process, i_calculos, i_empregados FROM {B}fobasesserv WHERE codi_emp = ? AND competencia = ? AND rateio = 0) t GROUP BY tipo_process", (empresa, ini))}
        tipos = m.doms.get("tipo_folha", {}).get("valores", {})
        out, tp, td, tl = [], 0.0, 0.0, 0.0
        for x in base:
            pv, dc = _n(x["proventos"]), _n(x["descontos"])
            l = liq.get(x["tipo_process"])
            item = {"tipo_folha": {"codigo": x["tipo_process"], "significado": tipos.get(x["tipo_process"])}, "empregados": x["empregados"], "proventos": pv, "descontos": dc,
                    "liquido_calculado": round(pv - dc, 2), "liquido_gravado": _n(l["liquido"]) if l else None,
                    "bases_sem_liquido": pares.get(x["tipo_process"], 0) - (l["pares"] if l else 0)}
            out.append(item)
            tp += pv; td += dc; tl += _n(l["liquido"]) if l else 0
        return {"empresa": empresa, "competencia": ini.isoformat()[:7], "por_tipo_de_folha": out,
                "totais": {"proventos": round(tp, 2), "descontos": round(td, 2), "liquido_calculado": round(tp - td, 2), "liquido_gravado": round(tl, 2)},
                "aviso": "Totais agregados da empresa (dado financeiro). `liquido_gravado` só existe onde houve pagamento registrado; tipos sem significado conhecido (60, 61, 92) aparecem como vêm do banco."}

    return m._executar("resumo_folha", {"empresa": empresa, "competencia": competencia}, run)


# ===================================================================================== histórico salarial do empregado
def historico_salarial(m: Motor, empresa: int, empregado: int) -> dict:
    """Linha do tempo salarial de um empregado: alterações salariais (salário anterior, novo, forma e motivo) e alterações contratuais (cargo, serviço, salário), com checagem
    de continuidade (o salário anterior de cada alteração deve ser o novo da anterior; fecha em 99,6% dos pares) e das contas de percentual e adição.

    Dado financeiro por pessoa identificável: uso restrito. Datas de 1900-01-01 são o valor padrão (início do contrato, não uma alteração real)."""
    empresa, empregado = int(empresa), int(empregado)

    def run():
        alt = m._sql(f"""SELECT competencia, forma_alteracao, salario_anterior, novo_salario, valor_adicionado, perc_aumento, motivo, retroativo, retroativo_data
                           FROM {B}foaltesal WHERE codi_emp = ? AND i_empregados = ? AND tipo_alt_grade = 1 ORDER BY competencia""", (empresa, empregado))
        con = m._sql(f"""SELECT a.data_alteracao, a.salario, a.i_cargos, a.i_servicos, a.horas_semana, c.nome AS cargo
                           FROM {B}foempregados_alteracao_contratual a LEFT JOIN {B}focargos c ON c.codi_emp = a.codi_emp AND c.i_cargos = a.i_cargos
                          WHERE a.codi_emp = ? AND a.i_empregados = ? ORDER BY a.data_alteracao""", (empresa, empregado))
        if not alt and not con:
            raise ErroUso(f"Nenhum histórico salarial para o empregado {empregado} da empresa {empresa}.")
        formas = m.doms.get("forma_alteracao_salarial", {}).get("valores", {})
        alteracoes, problemas, anterior = [], [], None
        for x in alt:
            novo, ant = _n(x["novo_salario"]), _n(x["salario_anterior"]) if x["salario_anterior"] is not None else None
            item = {"competencia": x["competencia"].isoformat()[:7] if x["competencia"] and x["competencia"].year >= 2000 else "não informada (1900-01-01)",
                    "forma": formas.get(x["forma_alteracao"], x["forma_alteracao"]), "salario_anterior": ant, "novo_salario": novo, "motivo": x["motivo"], "retroativa": x["retroativo"] == 1}
            if x["forma_alteracao"] == 3 and x["perc_aumento"] is not None and ant is not None:
                esperado = round(ant * (1 + float(x["perc_aumento"]) / 100), 2)
                item["percentual"] = float(x["perc_aumento"]); item["confere_percentual"] = abs(esperado - novo) < 0.05
            if x["forma_alteracao"] == 2 and x["valor_adicionado"] is not None and ant is not None:
                item["confere_adicao"] = abs(round(ant + _n(x["valor_adicionado"]), 2) - novo) < 0.05
            if anterior is not None and ant is not None and abs(anterior - ant) >= 0.05:
                problemas.append({"competencia": item["competencia"], "esperado_como_salario_anterior": anterior, "salario_anterior_gravado": ant})
            if ant is not None:
                anterior = novo
            elif anterior is None:
                anterior = novo
            alteracoes.append(item)
        contratos = [{"data": x["data_alteracao"].isoformat() if x["data_alteracao"] and x["data_alteracao"].year >= 2000 else "não informada (1900-01-01)", "salario": _n(x["salario"]),
                      "cargo": (x["cargo"] or "").strip() or None, "servico": x["i_servicos"], "horas_semana": float(x["horas_semana"]) if x["horas_semana"] is not None else None} for x in con]
        r = {"empresa": empresa, "empregado": empregado, "alteracoes_salariais": alteracoes, "alteracoes_contratuais": contratos,
             "salario_atual_pela_ultima_alteracao_salarial": alteracoes[-1]["novo_salario"] if alteracoes else None,
             "salario_atual_pela_ultima_alteracao_contratual": contratos[-1]["salario"] if contratos else None,
             "problemas_de_continuidade": problemas}
        if alteracoes and contratos and abs(r["salario_atual_pela_ultima_alteracao_salarial"] - r["salario_atual_pela_ultima_alteracao_contratual"]) >= 0.05:
            r["aviso"] = "O salário da última alteração salarial difere do da última alteração contratual: confira qual vale (o cadastro do empregado e o último cálculo de folha dizem qual foi usado)."
        return r

    return m._executar("historico_salarial", {"empresa": empresa, "empregado": empregado}, run)


# ===================================================================================== classificação fiscal de um produto
def classificacao_produto(m: Motor, empresa: int, produto: str, data: str | None = None) -> dict:
    """Classificação fiscal de um produto numa data: PIS/COFINS (CST, tipo de contribuição, natureza da receita, monofásico, alíquotas), ICMS, IPI e substituição tributária.

    Usa a vigência de maior data até a data pedida (mesma regra de acumuladores e parâmetros). O banco NÃO traz a legenda dos CST: aparecem só os códigos (a legenda oficial vem do layout fiscal, fora do banco); o NCM vem do cadastro."""
    empresa = int(empresa)
    produto = str(produto).strip()
    dia = _coagir(data) if data else datetime.date.today()
    if not isinstance(dia, datetime.date):
        raise ErroUso("data deve estar no formato AAAA-MM-DD.")

    def run():
        v = m._sql(f"""SELECT TOP 1 v.vigencia_pdi, v.descricao, v.codigo_cst_entrada, v.codigo_cst_saida, v.tipo_contribuicao, v.natureza_receita, v.produto_sujeito_tributacao_monofasica_piscofins,
                              v.aliquota_pis_debito, v.aliquota_cofins_debito, v.debito_aliquota_diferenciada, v.aliquota_pis_credito, v.aliquota_cofins_credito, v.dados_piscofins_ok,
                              v.cst_icms_entrada, v.cst_icms_saida, v.aliquota_icms, v.cst_ipi_entrada, v.cst_ipi_saida, v.aliquota_ipi, v.produto_incluido_st, v.base_calculo_st,
                              v.percentual_margem_de_valor_adic_st, v.percentual_reducao_bc_st, p.desc_pdi, p.cncm_pdi
                         FROM {B}efprodutos_vigencia v LEFT JOIN {B}efprodutos p ON p.codi_emp = v.codi_emp AND p.codi_pdi = v.codi_pdi
                        WHERE v.codi_emp = ? AND TRIM(v.codi_pdi) = ? AND v.vigencia_pdi <= ? ORDER BY v.vigencia_pdi DESC""", (empresa, produto, dia))
        if not v:
            raise ErroUso(f"Produto '{produto}' da empresa {empresa} sem classificação fiscal em vigor em {dia.isoformat()} (código inexistente ou vigência posterior).")
        x = v[0]
        outras = m._sql(f"SELECT COUNT(*) AS n FROM {B}efprodutos_vigencia WHERE codi_emp = ? AND TRIM(codi_pdi) = ?", (empresa, produto))[0]["n"]
        tipos = m.doms.get("tipo_contribuicao_produto", {}).get("valores", {})
        cst = m.doms.get("cst_pis_cofins", {}).get("valores", {})
        r = {"empresa": empresa, "produto": produto, "data": dia.isoformat(), "vigencia_em_uso": x["vigencia_pdi"].isoformat(), "vigencias_do_produto": outras,
             "descricao": (x["descricao"] or x["desc_pdi"] or "").strip(), "ncm": (x["cncm_pdi"] or "").strip() or None,
             "pis_cofins": {"cst_saida": {"codigo": x["codigo_cst_saida"], "significado": cst.get(x["codigo_cst_saida"])},
                            "cst_entrada": {"codigo": x["codigo_cst_entrada"], "significado": cst.get(x["codigo_cst_entrada"])},
                            "tipo_contribuicao": {"codigo": x["tipo_contribuicao"], "significado": tipos.get((x["tipo_contribuicao"] or "").strip())},
                            "natureza_da_receita": x["natureza_receita"], "monofasico": (x["produto_sujeito_tributacao_monofasica_piscofins"] or "").strip() == "S",
                            "aliquota_diferenciada_saida": (x["debito_aliquota_diferenciada"] or "").strip() == "S",
                            "aliquota_pis_saida": float(x["aliquota_pis_debito"] or 0), "aliquota_cofins_saida": float(x["aliquota_cofins_debito"] or 0),
                            "dados_conferidos": (x["dados_piscofins_ok"] or "").strip() == "S"},
             "icms": {"cst_entrada": x["cst_icms_entrada"], "cst_saida": x["cst_icms_saida"], "aliquota": float(x["aliquota_icms"] or 0)},
             "ipi": {"cst_entrada": x["cst_ipi_entrada"], "cst_saida": x["cst_ipi_saida"], "aliquota": float(x["aliquota_ipi"] or 0)},
             "substituicao_tributaria": {"produto_incluido": (x["produto_incluido_st"] or "").strip() == "S", "base_de_calculo": (x["base_calculo_st"] or "").strip() or None,
                                         "margem_valor_agregado": float(x["percentual_margem_de_valor_adic_st"] or 0), "reducao_base": float(x["percentual_reducao_bc_st"] or 0)}}
        avisos = []
        if not r["pis_cofins"]["dados_conferidos"]:
            avisos.append("Os dados de PIS/COFINS deste produto não estão marcados como conferidos (dados_piscofins_ok = N): a apuração pode sinalizar o item.")
        if x["vigencia_pdi"].year < 2000:
            avisos.append("A vigência é anterior a 2000 (provável valor padrão 1964-06-01).")
        if avisos:
            r["avisos"] = avisos
        return r

    return m._executar("classificacao_produto", {"empresa": empresa, "produto": produto, "data": data}, run)


# ===================================================================================== visão mensal consolidada da empresa
def visao_mensal(m: Motor, empresa: int, competencia: str) -> dict:
    """Visão do mês da empresa numa só resposta: receita bruta, guias de impostos, folha de pagamento e o estado das obrigações (eSocial, EFD-Reinf e, no Simples, DAS/PGDAS-D).

    Chama as funções já conferidas (receita_bruta_mensal, guias_do_mes, resumo_folha, situacao_esocial, situacao_reinf, situacao_das) e junta os alertas. Um bloco que não se
    aplica à empresa (ex.: sem folha) vem como null com o motivo em `observacoes`. Dados financeiros da empresa."""
    empresa = int(empresa)
    ini, _ = _mes(competencia)
    mes = ini.isoformat()[:7]
    out = {"empresa": empresa, "competencia": mes}
    obs, alertas = [], []

    def bloco(nome, fn, *args):
        try:
            return fn(m, *args)
        except ErroUso as ex:
            obs.append(f"{nome}: {ex}")
            return None

    perfil = bloco("perfil", perfil_empresa, empresa, ini.isoformat())
    out["empresa_nome"] = perfil["cadastro"]["nome"] if perfil else None
    reg = (perfil or {}).get("fiscal") or {}
    codigo_regime = (reg.get("regime_federal") or {}).get("codigo")
    out["regime_federal"] = reg.get("regime_federal")
    rec = bloco("receita", receita_bruta_mensal, empresa, mes, mes)
    out["receita_bruta"] = rec["meses"][0] if rec else None
    g = bloco("guias", guias_do_mes, empresa, mes)
    out["guias"] = {"totais": g["totais"], "quantidade": len(g["guias"]), "situacoes": sorted({x["situacao"] for x in g["guias"]})} if g else None
    if g and g["totais"]["saldo_a_recolher"] > 0 and ini >= datetime.date(2024, 1, 1):
        alertas.append(f"Guias: há {g['totais']['saldo_a_recolher']:.2f} a recolher em {len(g['guias'])} guia(s) de impostos; o registro de pagamentos do sistema não é confiável a partir de 2024, confirme o pagamento.")
    fo = bloco("folha", resumo_folha, empresa, mes)
    out["folha"] = fo["totais"] if fo else None
    es = bloco("esocial", situacao_esocial, empresa, mes)
    out["esocial"] = {"fechamento": es["fechamento_da_folha"]["estado"], "eventos": es["eventos_da_competencia"], "eventos_sem_recibo_da_empresa": es["pendencias"]["eventos_sem_recibo_da_empresa"]} if es else None
    if es and fo and es["fechamento_da_folha"]["estado"] != "fechada":
        alertas.append(f"Há folha calculada em {mes}, mas o eSocial não está fechado (estado: {es['fechamento_da_folha']['estado']}).")
    if es and any(e["rejeitados"] for e in es["eventos_da_competencia"]):
        alertas.append("eSocial: há eventos rejeitados nesta competência.")
    re_ = bloco("reinf", situacao_reinf, empresa, mes)
    out["reinf"] = {"fechamento": re_["fechamento_serie_2000"]["estado"], "eventos": re_["eventos"]} if re_ else None
    if re_ and re_["eventos"] and re_["fechamento_serie_2000"]["estado"] != "fechada":
        alertas.append(f"Há eventos da EFD-Reinf em {mes}, mas a série R-2000 não está fechada (estado: {re_['fechamento_serie_2000']['estado']}).")
    if codigo_regime in (2, 4):
        das = bloco("das", situacao_das, empresa, mes)
        out["das"] = {"estado": das["estado"], "apuracao_simples": das["apuracao_simples"], "guia": das["guia_das"]} if das else None
        if das and any(a.startswith("ATENÇÃO") for a in das.get("avisos", [])):
            alertas += [f"DAS: {a}" for a in das["avisos"] if a.startswith("ATENÇÃO")]
        sim = bloco("receita_simples", receita_bruta_simples, empresa, mes)
        if sim and sim["situacao"] == "diverge":
            alertas.append(f"Simples: a receita dos documentos ({sim['recalculado']['receita_bruta']:.2f}) difere da base apurada ({sim['apurado_pela_dominio']['base_calculo']:.2f}) em {sim['diferenca']:.2f}.")
        out["receita_vs_simples"] = {"situacao": sim["situacao"], "diferenca": sim.get("diferenca")} if sim else None
    elif codigo_regime == 5 or codigo_regime == 1:
        out["das"] = None
    inf = bloco("informativos", informativos_da_empresa, empresa, mes, mes)
    out["informativos_do_mes"] = inf["por_informativo"] if inf else None
    out["alertas"] = alertas
    if obs:
        out["observacoes"] = obs
    return m._executar("visao_mensal", {"empresa": empresa, "competencia": competencia}, lambda: out)


# ===================================================================================== catálogo de funções
FUNCOES: dict[str, dict] = {
    "receita_bruta_simples": {
        "executar": receita_bruta_simples,
        "descricao": (receita_bruta_simples.__doc__ or "").strip().split("\n\n")[0],
        "parametros": {"empresa": "código da empresa (int)", "competencia": "mês no formato AAAA-MM"},
        "fontes": ["efsaidas", "efservicos", "efcupom_fiscal_eletronico_impostos", "efentradas", "efacumulador_vigencia", "efsdoimp_simples_nacional"],
        "validada": "38 de 40 empresa/competências da amostra aleatória fecham ao centavo (scripts/conciliar_receita_simples.py).",
    },
    "perfil_fiscal": {
        "executar": perfil_fiscal,
        "descricao": (perfil_fiscal.__doc__ or "").strip().split("\n\n")[0],
        "parametros": {"empresa": "código da empresa (int)", "data": "data AAAA-MM-DD (padrão: hoje)"},
        "fontes": ["efparametro_vigencia", "efparametro_vigencia_impostos", "geimposto", "efsdoimp_simples_nacional", "efsdoimp"],
        "validada": "regimes 4 (Simples), 5 (presumido) e 2 (variante do Simples) deduzidos dos dados; 1 provável real; 6, 8 e 9 não determinados.",
    },
    "informativos_da_empresa": {
        "executar": informativos_da_empresa,
        "descricao": "Informativos (obrigações acessórias) preparados para a empresa no período, com campos informados, retificadora e número de recibo.",
        "parametros": {"empresa": "código da empresa (int)", "de": "mês inicial AAAA-MM", "ate": "opcional: mês final AAAA-MM (padrão: igual a de)", "informativo": "opcional: código do informativo (veja a entidade informativo)"},
        "fontes": ["efoutrosdados", "efoutrosdados_dados", "efinformativos"],
        "validada": "todo campo tem cabeçalho (0 órfãos em 3,8 mi); recibo e retificadora só existem em alguns informativos.",
    },
    "apuracao_lalur": {
        "executar": apuracao_lalur,
        "descricao": "Apuração do IRPJ e da CSLL pelo lucro real (Lalur) numa competência, com conferência das identidades do cálculo.",
        "parametros": {"empresa": "código da empresa (int)", "competencia": "mês AAAA-MM"},
        "fontes": ["lrcalculo", "lrcalculo_irpj_real", "lrcalculo_csll_real", "lrlucro_antes_csll_irpj"],
        "validada": "lucro real, base, 15%, 9%, adicional e valor a recolher (piso zero) fecham em 100% dos 3.108 cálculos; deduções da CSLL em 3.103.",
    },
    "situacao_das": {
        "executar": situacao_das,
        "descricao": "Situação do DAS (Simples Nacional) numa competência: apuração, declaração PGDAS-D transmitida pela API, guia DAS emitida e erros recentes.",
        "parametros": {"empresa": "código da empresa (int)", "competencia": "mês AAAA-MM"},
        "fontes": ["efsdoimp_simples_nacional", "efdas_api_envio_arquivos", "efdas_api_envio_arquivos_mensagem"],
        "validada": "legenda da situação (0-4) bate 1 para 1 com os códigos HTTP das mensagens; retificadora = a partir da 2ª transmissão com sucesso (1.334 de 1.334). Só a partir de 2024-04.",
    },
    "receita_bruta_mensal": {
        "executar": receita_bruta_mensal,
        "descricao": "Receita bruta mês a mês (até 36 meses): saídas + serviços + CF-e de acumuladores que incidem sobre receita bruta, menos devoluções; para o Simples traz também a base apurada.",
        "parametros": {"empresa": "código da empresa (int)", "de": "mês inicial AAAA-MM", "ate": "mês final AAAA-MM"},
        "fontes": ["efsaidas", "efservicos", "efcupom_fiscal_eletronico_impostos", "efentradas", "efacumulador_vigencia", "efsdoimp_simples_nacional"],
        "validada": "mesma regra de receita_bruta_simples (38 de 40 competências do Simples fecham ao centavo).",
    },
    "situacao_reinf": {
        "executar": situacao_reinf,
        "descricao": "Situação da EFD-Reinf numa competência: fechamento (R-2099/R-2098), eventos enviados, aceitos, rejeitados e aguardando, e rejeições recentes.",
        "parametros": {"empresa": "código da empresa (int)", "competencia": "mês AAAA-MM"},
        "fontes": ["efd_reinf_envio_arquivos", "efd_reinf_envio_arquivos_erros"],
        "validada": "aceito = situação 1 com recibo (99,7%); rejeitado = situação 3 (99,8% com erro); fechamento = último R-2098/R-2099 aceito.",
    },
    "resumo_folha": {
        "executar": resumo_folha,
        "descricao": "Totais da folha numa competência por tipo de folha: empregados, proventos, descontos e líquido (agregados, sem identificar empregados).",
        "parametros": {"empresa": "código da empresa (int)", "competencia": "mês AAAA-MM"},
        "fontes": ["fobasesserv", "foliquidosfilepr"],
        "validada": "líquido gravado = proventos - descontos em 254 de 254 cálculos/empregados (empresa 354, 2025+). Dado financeiro.",
    },
    "historico_salarial": {
        "executar": historico_salarial,
        "descricao": "Linha do tempo salarial de um empregado (alterações salariais e contratuais) com checagem de continuidade e das contas de percentual e adição.",
        "parametros": {"empresa": "código da empresa (int)", "empregado": "código do empregado (int)"},
        "fontes": ["foaltesal", "foempregados_alteracao_contratual", "focargos"],
        "validada": "percentual 3.727/3.731; adição 107/107; continuidade 8.915/8.955. Dado financeiro por pessoa identificável.",
    },
    "classificacao_produto": {
        "executar": classificacao_produto,
        "descricao": "Classificação fiscal de um produto numa data: PIS/COFINS (CST, tipo de contribuição, monofásico, alíquotas), ICMS, IPI e substituição tributária.",
        "parametros": {"empresa": "código da empresa (int)", "produto": "código do produto (texto)", "data": "data AAAA-MM-DD (padrão: hoje)"},
        "fontes": ["efprodutos_vigencia", "efprodutos"],
        "validada": "vigência em uso = a mais recente até a data; todas as vigências das 5 maiores empresas têm o produto no cadastro (0 sem cadastro em 71.973).",
    },
    "visao_mensal": {
        "executar": visao_mensal,
        "descricao": "Visão do mês da empresa numa só resposta: receita bruta, guias, folha e estado das obrigações (eSocial, EFD-Reinf e, no Simples, DAS), com alertas.",
        "parametros": {"empresa": "código da empresa (int)", "competencia": "mês AAAA-MM"},
        "fontes": ["receita_bruta_mensal", "guias_do_mes", "resumo_folha", "situacao_esocial", "situacao_reinf", "situacao_das", "receita_bruta_simples", "informativos_da_empresa", "perfil_empresa"],
        "validada": "compõe funções já conferidas; blocos que não se aplicam vêm como null com o motivo.",
    },
    "perfil_empresa": {
        "executar": perfil_empresa,
        "descricao": "Perfil completo da empresa: cadastro, regimes e impostos, parâmetros da contabilidade e da folha, e último fechamento no eSocial.",
        "parametros": {"empresa": "código da empresa (int)", "data": "data AAAA-MM-DD (padrão: hoje)"},
        "fontes": ["geempre", "efparametro_vigencia", "ctparmto", "foparmto", "foempregados", "foesocial_dados_eventos"],
        "validada": "junta funções e entidades já conferidas; blocos ausentes vêm como null com o motivo.",
    },
    "guias_do_mes": {
        "executar": guias_do_mes,
        "descricao": "Guias de impostos da empresa numa competência: imposto, código de recolhimento, vencimento, saldo a recolher, valor pago e situação.",
        "parametros": {"empresa": "código da empresa (int)", "competencia": "mês AAAA-MM", "incluir_sem_saldo": "opcional: inclui apurações sem saldo a recolher"},
        "fontes": ["efsdoimp_por_recolhimento", "efpagimp", "geimposto"],
        "validada": "valor pago fecha com a soma dos pagamentos em 98,2% (2.044 de 2.082 guias, 2023-2024); registro de pagamentos incompleto a partir de 2024 (avisado na resposta).",
    },
    "memoria_calculo_folha": {
        "executar": memoria_calculo_folha,
        "descricao": "Memória de cálculo da folha de um empregado numa competência: cada base (INSS, FGTS, IRRF, férias...) com base, taxa e valor.",
        "parametros": {"empresa": "código da empresa (int)", "empregado": "código do empregado (int)", "competencia": "mês AAAA-MM", "tipo_folha": "opcional: código do tipo de folha (ex.: 11 = mensal)"},
        "fontes": ["fobasesserv", "focalculosbases", "focadbases"],
        "validada": "valor = base x taxa / 100 em 86,6% das bases com taxa (empresa 354, 2026); as demais são progressivas ou com dedução. Dado financeiro por pessoa: uso restrito.",
    },
    "situacao_esocial": {
        "executar": situacao_esocial,
        "descricao": (situacao_esocial.__doc__ or "").strip().split("\n\n")[0],
        "parametros": {"empresa": "código da empresa (int)", "competencia": "mês no formato AAAA-MM"},
        "fontes": ["foesocial_dados_eventos", "foesocial_eventos"],
        "validada": "fechamento = último S-1298/S-1299 da competência (padrão fechar-reabrir-fechar visto nos dados); aceite = recibo + validado = 1 (99,99% dos registros).",
    },
}


def executar(m: Motor, nome: str, **kwargs) -> dict:
    if nome not in FUNCOES:
        raise ErroUso(f"Função '{nome}' não existe. Disponíveis: {', '.join(FUNCOES)}")
    return FUNCOES[nome]["executar"](m, **kwargs)

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_natureza_acao_processo_referenciado (Tabela de natureza da ação dos processos referenciados) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_natureza_acao_processo_referenciado"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_natureza_acao_processo_referenciado']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctatendimento_plano_contas_controle_websocket (Gerencia os retornos da integração com a Conta Azul no agente de comunicação, incluindo envios, avisos, erros e suporte a reenvio.) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctatendimento_plano_contas_controle_websocket"
MODULO = "contabil_outros"
ENTIDADES = ['ctatendimento_plano_contas_controle_websocket']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

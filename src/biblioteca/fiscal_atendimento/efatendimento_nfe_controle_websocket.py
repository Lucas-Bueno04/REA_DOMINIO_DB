# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efatendimento_nfe_controle_websocket (EFATENDIMENTO_NFE_CONTROLE_WEBSOCKET) - módulo fiscal_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efatendimento_nfe_controle_websocket"
MODULO = "fiscal_atendimento"
ENTIDADES = ['efatendimento_nfe_controle_websocket']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

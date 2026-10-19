# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimentowebsocket_onvio_rota_conta_iceberg (Armazena mensagens recebidos pelo websocket referente a rota que busca as contas financeiras do Iceberg) - módulo geral_atendimentowebsocket."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimentowebsocket_onvio_rota_conta_iceberg"
MODULO = "geral_atendimentowebsocket"
ENTIDADES = ['geatendimentowebsocket_onvio_rota_conta_iceberg']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

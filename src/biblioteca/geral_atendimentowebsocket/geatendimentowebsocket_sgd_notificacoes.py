# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimentowebsocket_sgd_notificacoes (Notificações de suporte e notícias recebidas pelo websocket) - módulo geral_atendimentowebsocket."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimentowebsocket_sgd_notificacoes"
MODULO = "geral_atendimentowebsocket"
ENTIDADES = ['geatendimentowebsocket_sgd_notificacoes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

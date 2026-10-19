# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_sgd_notificacoes (Notificações de suporte e notícias) - módulo geral_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_sgd_notificacoes"
MODULO = "geral_atendimento"
ENTIDADES = ['geatendimento_sgd_notificacoes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

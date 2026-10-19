# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_dados_escritorio_historico (Tabela de histórico de mudança da tabela GEATENDIMENTO_DADOS_ESCRITORIO) - módulo geral_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_dados_escritorio_historico"
MODULO = "geral_atendimento"
ENTIDADES = ['geatendimento_dados_escritorio_historico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

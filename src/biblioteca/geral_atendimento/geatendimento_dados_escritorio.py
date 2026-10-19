# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_dados_escritorio (Dados obtidos do SGD à respeito do escritório) - módulo geral_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_dados_escritorio"
MODULO = "geral_atendimento"
ENTIDADES = ['geatendimento_dados_escritorio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

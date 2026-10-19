# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsimples_nacional_informacao_estadual (Informações Estaduais do Simples Nacional) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsimples_nacional_informacao_estadual"
MODULO = "fiscal_outros"
ENTIDADES = ['efsimples_nacional_informacao_estadual']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

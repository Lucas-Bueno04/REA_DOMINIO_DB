# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsped_contas_analiticas (Contas SPED Analíticas) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsped_contas_analiticas"
MODULO = "fiscal_outros"
ENTIDADES = ['efsped_contas_analiticas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

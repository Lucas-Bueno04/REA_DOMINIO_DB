# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsped_fiscal_e311 (Contém os códigos referente ao registro E311) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsped_fiscal_e311"
MODULO = "fiscal_outros"
ENTIDADES = ['efsped_fiscal_e311']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

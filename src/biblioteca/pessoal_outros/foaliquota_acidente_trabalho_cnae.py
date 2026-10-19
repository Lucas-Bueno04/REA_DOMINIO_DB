# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foaliquota_acidente_trabalho_cnae (Tabela de catálogo dos valores de alíquota conforme acidente de trabalho CNAE) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foaliquota_acidente_trabalho_cnae"
MODULO = "pessoal_outros"
ENTIDADES = ['foaliquota_acidente_trabalho_cnae']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

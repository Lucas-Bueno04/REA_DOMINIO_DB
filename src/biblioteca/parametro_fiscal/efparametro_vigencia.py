# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efparametro_vigencia (Parâmetros da escrita fiscal por vigência) - módulo parametro_fiscal."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efparametro_vigencia"
MODULO = "parametro_fiscal"
ENTIDADES = ['parametro_fiscal']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

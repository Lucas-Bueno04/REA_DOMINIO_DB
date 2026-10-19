# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foparmto (Parâmetros da folha por empresa) - módulo parametros_empresa."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foparmto"
MODULO = "parametros_empresa"
ENTIDADES = ['parametro_folha']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabelamuni (Tabelas Municipais - Cadastro) - módulo fiscal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabelamuni"
MODULO = "fiscal_nucleo"
ENTIDADES = ['eftabelamuni']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

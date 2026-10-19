# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomovtoserv_salario_familia (Dependentes que foram considerados para o cálculo do salário família na rubrica.) - módulo pessoal_movtoserv."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomovtoserv_salario_familia"
MODULO = "pessoal_movtoserv"
ENTIDADES = ['fomovtoserv_salario_familia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

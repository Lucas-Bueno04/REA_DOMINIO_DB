# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focalculos_diferenca_rais (Todos os calculos com diferença de salario por competência.) - módulo pessoal_calculos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focalculos_diferenca_rais"
MODULO = "pessoal_calculos"
ENTIDADES = ['focalculos_diferenca_rais']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

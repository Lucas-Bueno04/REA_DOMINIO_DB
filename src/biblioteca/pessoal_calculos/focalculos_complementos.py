# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focalculos_complementos (Complementos de cálculo) - módulo pessoal_calculos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focalculos_complementos"
MODULO = "pessoal_calculos"
ENTIDADES = ['focalculos_complementos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focalculos (Calculo - Sequencia de calculos) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focalculos"
MODULO = "pessoal_nucleo"
ENTIDADES = ['focalculos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

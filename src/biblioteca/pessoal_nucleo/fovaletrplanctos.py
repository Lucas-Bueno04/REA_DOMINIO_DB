# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fovaletrplanctos (Vale transporte - Lancamentos) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fovaletrplanctos"
MODULO = "pessoal_nucleo"
ENTIDADES = ['fovaletrplanctos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

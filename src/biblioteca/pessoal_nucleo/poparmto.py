# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela poparmto (Parametros do Ponto) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "poparmto"
MODULO = "pessoal_nucleo"
ENTIDADES = ['poparmto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

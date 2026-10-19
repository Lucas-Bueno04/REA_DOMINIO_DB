# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focodigos_gps (Tabela de códigos GPS) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focodigos_gps"
MODULO = "pessoal_outros"
ENTIDADES = ['focodigos_gps']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

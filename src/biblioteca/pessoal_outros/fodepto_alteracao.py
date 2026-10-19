# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fodepto_alteracao (Alterações da tabela do departamento.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fodepto_alteracao"
MODULO = "pessoal_outros"
ENTIDADES = ['fodepto_alteracao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

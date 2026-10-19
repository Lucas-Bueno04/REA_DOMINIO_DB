# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctdepto (Departamentos (contabilidade)) - módulo contabil."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctdepto"
MODULO = "contabil"
ENTIDADES = ['departamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

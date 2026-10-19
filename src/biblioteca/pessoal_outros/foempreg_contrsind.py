# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foempreg_contrsind (Empregados - Cadastro - Contribuicao Sindical) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foempreg_contrsind"
MODULO = "pessoal_outros"
ENTIDADES = ['foempreg_contrsind']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

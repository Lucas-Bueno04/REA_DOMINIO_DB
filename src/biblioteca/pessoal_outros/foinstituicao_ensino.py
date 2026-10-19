# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foinstituicao_ensino (Cadastro de instituições de ensino.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foinstituicao_ensino"
MODULO = "pessoal_outros"
ENTIDADES = ['foinstituicao_ensino']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fosituacoes_avo_13 (Situações dos avos do 13º salário) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fosituacoes_avo_13"
MODULO = "pessoal_outros"
ENTIDADES = ['fosituacoes_avo_13']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

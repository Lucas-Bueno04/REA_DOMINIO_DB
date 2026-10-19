# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrincentivo_fiscal (Cadastro de Incentivos Fiscais) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrincentivo_fiscal"
MODULO = "contabil_outros"
ENTIDADES = ['lrincentivo_fiscal']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

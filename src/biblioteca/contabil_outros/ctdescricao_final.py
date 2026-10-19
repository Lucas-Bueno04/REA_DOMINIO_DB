# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctdescricao_final (Descricao final para demonstrativos) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctdescricao_final"
MODULO = "contabil_outros"
ENTIDADES = ['ctdescricao_final']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

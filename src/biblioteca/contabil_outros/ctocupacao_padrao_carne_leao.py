# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctocupacao_padrao_carne_leao (Parametro Contabilidade) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctocupacao_padrao_carne_leao"
MODULO = "contabil_outros"
ENTIDADES = ['ctocupacao_padrao_carne_leao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

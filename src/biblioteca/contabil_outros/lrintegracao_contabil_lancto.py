# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrintegracao_contabil_lancto (Integração Contábil Lalur - Lançamentos Contábeis) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrintegracao_contabil_lancto"
MODULO = "contabil_outros"
ENTIDADES = ['lrintegracao_contabil_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

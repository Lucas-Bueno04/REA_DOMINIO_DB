# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctorigem_lancamento (Origem dos lançamentos da contabilidade) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctorigem_lancamento"
MODULO = "contabil_outros"
ENTIDADES = ['ctorigem_lancamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

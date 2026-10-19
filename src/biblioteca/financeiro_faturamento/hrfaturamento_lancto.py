# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrfaturamento_lancto (Faturamento X Lancamentos Contabeis) - módulo financeiro_faturamento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrfaturamento_lancto"
MODULO = "financeiro_faturamento"
ENTIDADES = ['hrfaturamento_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

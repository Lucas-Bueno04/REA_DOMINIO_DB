# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrfaturamento_adicional (Faturamento - Adicional) - módulo financeiro_faturamento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrfaturamento_adicional"
MODULO = "financeiro_faturamento"
ENTIDADES = ['hrfaturamento_adicional']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

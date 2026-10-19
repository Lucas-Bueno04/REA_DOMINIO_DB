# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmovimento_ajuste_federal (Ajuste Impostos lançados federais - Geral) - módulo fiscal_movimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmovimento_ajuste_federal"
MODULO = "fiscal_movimento"
ENTIDADES = ['efmovimento_ajuste_federal']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

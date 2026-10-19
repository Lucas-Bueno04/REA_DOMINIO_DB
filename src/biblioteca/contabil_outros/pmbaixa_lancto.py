# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmbaixa_lancto (Baixas - Parcial e total - Lançamentos Contábeis) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmbaixa_lancto"
MODULO = "contabil_outros"
ENTIDADES = ['pmbaixa_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

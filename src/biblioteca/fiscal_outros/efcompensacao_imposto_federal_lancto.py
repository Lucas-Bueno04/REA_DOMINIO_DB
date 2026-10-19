# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcompensacao_imposto_federal_lancto (Compensações de Impostos Federais - Lançamentos) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcompensacao_imposto_federal_lancto"
MODULO = "fiscal_outros"
ENTIDADES = ['efcompensacao_imposto_federal_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

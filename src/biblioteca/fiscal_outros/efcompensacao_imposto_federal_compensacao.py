# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcompensacao_imposto_federal_compensacao (Compensações de Impostos Federais - Compensação) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcompensacao_imposto_federal_compensacao"
MODULO = "fiscal_outros"
ENTIDADES = ['efcompensacao_imposto_federal_compensacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

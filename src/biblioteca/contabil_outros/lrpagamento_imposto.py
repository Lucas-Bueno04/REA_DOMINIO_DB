# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrpagamento_imposto (Pagamento de impostos do Lalur) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrpagamento_imposto"
MODULO = "contabil_outros"
ENTIDADES = ['lrpagamento_imposto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

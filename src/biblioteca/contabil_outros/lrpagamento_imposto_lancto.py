# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrpagamento_imposto_lancto (Pagamento de impostos do Lalur - Lancamentos Contabeis) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrpagamento_imposto_lancto"
MODULO = "contabil_outros"
ENTIDADES = ['lrpagamento_imposto_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

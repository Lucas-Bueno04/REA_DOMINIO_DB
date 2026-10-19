# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrfaturamento_parcela_item_detalhamento (Faturamento - Parcelas - Itens - Detalhamento) - módulo financeiro_faturamento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrfaturamento_parcela_item_detalhamento"
MODULO = "financeiro_faturamento"
ENTIDADES = ['hrfaturamento_parcela_item_detalhamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

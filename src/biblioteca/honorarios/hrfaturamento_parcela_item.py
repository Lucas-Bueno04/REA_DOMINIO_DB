# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrfaturamento_parcela_item (Itens das parcelas) - módulo honorarios."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrfaturamento_parcela_item"
MODULO = "honorarios"
ENTIDADES = ['item_parcela']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

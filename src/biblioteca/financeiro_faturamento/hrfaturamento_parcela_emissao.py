# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrfaturamento_parcela_emissao (Faturamento - Parcelas - Emissoes e exclusoes de boletos e documento de cobranca) - módulo financeiro_faturamento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrfaturamento_parcela_emissao"
MODULO = "financeiro_faturamento"
ENTIDADES = ['hrfaturamento_parcela_emissao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

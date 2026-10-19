# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrcontrato_historico (Contratos - Historicos) - módulo financeiro_contrato."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrcontrato_historico"
MODULO = "financeiro_contrato"
ENTIDADES = ['hrcontrato_historico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_rs_utilizacao_credito (Tabela de relacionamento - RS - Utilização de Crédito) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_rs_utilizacao_credito"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_rs_utilizacao_credito']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

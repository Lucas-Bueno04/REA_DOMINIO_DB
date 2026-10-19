# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrfaturamento_evento_renegociacao (Faturamento - Eventos oriundos da renegociacao) - módulo financeiro_faturamento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrfaturamento_evento_renegociacao"
MODULO = "financeiro_faturamento"
ENTIDADES = ['hrfaturamento_evento_renegociacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

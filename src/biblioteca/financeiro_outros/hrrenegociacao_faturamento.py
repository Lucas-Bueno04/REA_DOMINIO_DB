# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrrenegociacao_faturamento (Renegociacao - Faturamento) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrrenegociacao_faturamento"
MODULO = "financeiro_outros"
ENTIDADES = ['hrrenegociacao_faturamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

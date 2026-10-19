# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrrenegociacao_recebimento (Renegociacao - Recebimento) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrrenegociacao_recebimento"
MODULO = "financeiro_outros"
ENTIDADES = ['hrrenegociacao_recebimento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

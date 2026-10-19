# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsimples_nacional_folha_anterior (Simples Nacional - Valores da folha dos peridoso anteriores) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsimples_nacional_folha_anterior"
MODULO = "fiscal_outros"
ENTIDADES = ['efsimples_nacional_folha_anterior']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

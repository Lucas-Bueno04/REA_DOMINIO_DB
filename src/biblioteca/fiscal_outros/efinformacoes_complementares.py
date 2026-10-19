# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efinformacoes_complementares (Impostos) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efinformacoes_complementares"
MODULO = "fiscal_outros"
ENTIDADES = ['efinformacoes_complementares']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

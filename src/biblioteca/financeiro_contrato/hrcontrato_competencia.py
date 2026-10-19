# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrcontrato_competencia (Contratos - Competencias para faturamento futuro) - módulo financeiro_contrato."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrcontrato_competencia"
MODULO = "financeiro_contrato"
ENTIDADES = ['hrcontrato_competencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

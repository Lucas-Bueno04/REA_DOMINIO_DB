# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrcontrato_alteracao (Contratos - Alterações) - módulo financeiro_contrato."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrcontrato_alteracao"
MODULO = "financeiro_contrato"
ENTIDADES = ['hrcontrato_alteracao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

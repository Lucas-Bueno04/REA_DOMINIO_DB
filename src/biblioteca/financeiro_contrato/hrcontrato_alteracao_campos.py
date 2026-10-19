# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrcontrato_alteracao_campos (Contratos - Campos alterações) - módulo financeiro_contrato."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrcontrato_alteracao_campos"
MODULO = "financeiro_contrato"
ENTIDADES = ['hrcontrato_alteracao_campos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

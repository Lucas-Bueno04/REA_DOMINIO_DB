# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrreajuste_contrato (Reajuste de contratos) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrreajuste_contrato"
MODULO = "financeiro_outros"
ENTIDADES = ['hrreajuste_contrato']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

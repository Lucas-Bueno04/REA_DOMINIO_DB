# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_motivo_desoneracao_icms (Motivo desoneração do ICMS) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_motivo_desoneracao_icms"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_motivo_desoneracao_icms']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

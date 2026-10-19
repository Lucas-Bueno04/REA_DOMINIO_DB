# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_suspensao_impostos_federais_motivo_suspensao (Tabela de motivo de suspenção - Suspensão de impostos federais) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_suspensao_impostos_federais_motivo_suspensao"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_suspensao_impostos_federais_motivo_suspensao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

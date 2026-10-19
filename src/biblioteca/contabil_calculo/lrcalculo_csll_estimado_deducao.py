# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrcalculo_csll_estimado_deducao (Cálculo do Lalur - Imposto CSLL Estimado - Detalhamento de Deduções) - módulo contabil_calculo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrcalculo_csll_estimado_deducao"
MODULO = "contabil_calculo"
ENTIDADES = ['lrcalculo_csll_estimado_deducao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

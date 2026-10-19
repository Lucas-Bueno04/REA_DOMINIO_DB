# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrcalculo_csll_real_adicao (Cálculo do Lalur - Imposto CSLL Real - Detalhamento de Adições) - módulo contabil_calculo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrcalculo_csll_real_adicao"
MODULO = "contabil_calculo"
ENTIDADES = ['lrcalculo_csll_real_adicao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

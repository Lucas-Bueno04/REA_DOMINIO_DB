# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrcalculo_irpj_incentivo_fiscal (Cálculo do Lalur - Imposto IRPJ - Detalhamento de Incentivos Fiscais) - módulo contabil_calculo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrcalculo_irpj_incentivo_fiscal"
MODULO = "contabil_calculo"
ENTIDADES = ['lrcalculo_irpj_incentivo_fiscal']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

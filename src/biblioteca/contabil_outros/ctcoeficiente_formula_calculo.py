# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcoeficiente_formula_calculo (Coeficientes de análises - Fórmula - Cálculo) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcoeficiente_formula_calculo"
MODULO = "contabil_outros"
ENTIDADES = ['ctcoeficiente_formula_calculo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

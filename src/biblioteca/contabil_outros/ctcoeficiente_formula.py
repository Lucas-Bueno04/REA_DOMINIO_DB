# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcoeficiente_formula (Coeficientes de análises - Fórmula) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcoeficiente_formula"
MODULO = "contabil_outros"
ENTIDADES = ['ctcoeficiente_formula']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

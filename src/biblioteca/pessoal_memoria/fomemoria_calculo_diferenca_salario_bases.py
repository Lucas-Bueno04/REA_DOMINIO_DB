# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomemoria_calculo_diferenca_salario_bases (Memória de cálculo de diferença de salário - Bases de cálculo) - módulo pessoal_memoria."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomemoria_calculo_diferenca_salario_bases"
MODULO = "pessoal_memoria"
ENTIDADES = ['fomemoria_calculo_diferenca_salario_bases']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

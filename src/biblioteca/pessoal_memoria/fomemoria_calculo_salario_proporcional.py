# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomemoria_calculo_salario_proporcional (Memória de cálculo do salário proporcional.) - módulo pessoal_memoria."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomemoria_calculo_salario_proporcional"
MODULO = "pessoal_memoria"
ENTIDADES = ['fomemoria_calculo_salario_proporcional']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotabcalc_salario_minimo_estadual_vigencias_categorias (Valores do salário mínimo estadual por categoria na vigência.) - módulo pessoal_tabcalc."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotabcalc_salario_minimo_estadual_vigencias_categorias"
MODULO = "pessoal_tabcalc"
ENTIDADES = ['fotabcalc_salario_minimo_estadual_vigencias_categorias']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

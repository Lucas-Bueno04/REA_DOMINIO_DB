# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fovigencia_unidade_calculo (Vigência para o tipo de unidade do cálculo das rubricas.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fovigencia_unidade_calculo"
MODULO = "pessoal_outros"
ENTIDADES = ['fovigencia_unidade_calculo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

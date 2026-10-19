# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela forequerimento_seguro_desemprego_salarios (Últimos salários para o requerimento de Seguro Desemprego) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "forequerimento_seguro_desemprego_salarios"
MODULO = "pessoal_outros"
ENTIDADES = ['forequerimento_seguro_desemprego_salarios']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

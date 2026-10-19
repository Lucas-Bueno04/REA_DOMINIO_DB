# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foinssdata (Data de contribuicao de INSS) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foinssdata"
MODULO = "pessoal_nucleo"
ENTIDADES = ['foinssdata']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

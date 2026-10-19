# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fopagtoparcial_sindicatos (Informações dos valores de contribuição dos sindicatos) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fopagtoparcial_sindicatos"
MODULO = "pessoal_outros"
ENTIDADES = ['fopagtoparcial_sindicatos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

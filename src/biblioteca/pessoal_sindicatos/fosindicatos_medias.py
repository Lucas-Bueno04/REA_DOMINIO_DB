# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fosindicatos_medias (CADASTRO DE SINDICATOS - MÉDIAS) - módulo pessoal_sindicatos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fosindicatos_medias"
MODULO = "pessoal_sindicatos"
ENTIDADES = ['fosindicatos_medias']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

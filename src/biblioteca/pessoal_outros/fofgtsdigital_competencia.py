# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fofgtsdigital_competencia (RETRATO ATUAL DAS COMPETENCIAS RETORNADAS PELA CONSULTA NO FGTS DIGITAL) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fofgtsdigital_competencia"
MODULO = "pessoal_outros"
ENTIDADES = ['fofgtsdigital_competencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

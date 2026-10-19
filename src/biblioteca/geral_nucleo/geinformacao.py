# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geinformacao (Informações a respeito do banco de dados para serem enviadas a Domínio) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geinformacao"
MODULO = "geral_nucleo"
ENTIDADES = ['geinformacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

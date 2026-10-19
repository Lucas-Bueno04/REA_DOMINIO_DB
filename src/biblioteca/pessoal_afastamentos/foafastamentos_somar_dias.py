# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foafastamentos_somar_dias (Informações sobre os afastamentos que devem somar para calcular a data folha.) - módulo pessoal_afastamentos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foafastamentos_somar_dias"
MODULO = "pessoal_afastamentos"
ENTIDADES = ['foafastamentos_somar_dias']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

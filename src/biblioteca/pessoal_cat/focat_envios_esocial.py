# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focat_envios_esocial (Envios dos CAT para o esocial) - módulo pessoal_cat."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focat_envios_esocial"
MODULO = "pessoal_cat"
ENTIDADES = ['focat_envios_esocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

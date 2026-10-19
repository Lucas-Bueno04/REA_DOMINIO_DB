# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foafastamentos_envios_esocial (Envios de afastamentos ao eSocial) - módulo pessoal_afastamentos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foafastamentos_envios_esocial"
MODULO = "pessoal_afastamentos"
ENTIDADES = ['foafastamentos_envios_esocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

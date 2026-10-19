# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fovigencias_servico_envios_esocial (Envios das vigências do cadastro de serviços ao eSocial) - módulo pessoal_vigencias."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fovigencias_servico_envios_esocial"
MODULO = "pessoal_vigencias"
ENTIDADES = ['fovigencias_servico_envios_esocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

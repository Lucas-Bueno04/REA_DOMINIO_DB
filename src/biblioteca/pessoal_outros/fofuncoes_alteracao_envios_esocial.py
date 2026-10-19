# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fofuncoes_alteracao_envios_esocial (Envios de alterações das funções ao eSocial) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fofuncoes_alteracao_envios_esocial"
MODULO = "pessoal_outros"
ENTIDADES = ['fofuncoes_alteracao_envios_esocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

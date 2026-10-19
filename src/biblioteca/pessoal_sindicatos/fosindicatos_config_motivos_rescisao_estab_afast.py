# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fosindicatos_config_motivos_rescisao_estab_afast (Configuração dos motivos de rescisão que utilizam a estabilidade por afastamento informada no sindicato.) - módulo pessoal_sindicatos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fosindicatos_config_motivos_rescisao_estab_afast"
MODULO = "pessoal_sindicatos"
ENTIDADES = ['fosindicatos_config_motivos_rescisao_estab_afast']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

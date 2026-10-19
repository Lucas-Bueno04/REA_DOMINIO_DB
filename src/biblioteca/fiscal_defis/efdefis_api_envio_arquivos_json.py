# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efdefis_api_envio_arquivos_json (DEFIS Api - Envio dos Arquivos - JSON) - módulo fiscal_defis."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efdefis_api_envio_arquivos_json"
MODULO = "fiscal_defis"
ENTIDADES = ['efdefis_api_envio_arquivos_json']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

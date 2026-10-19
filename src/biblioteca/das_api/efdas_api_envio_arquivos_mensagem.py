# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efdas_api_envio_arquivos_mensagem (Mensagens de retorno da API do DAS) - módulo das_api."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efdas_api_envio_arquivos_mensagem"
MODULO = "das_api"
ENTIDADES = ['mensagem_envio_das_api']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

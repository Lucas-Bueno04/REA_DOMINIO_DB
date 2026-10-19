# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmit_api_envio_arquivos_mensagem (MIT API Integra Contador - Envio dos Arquivos - Retorno) - módulo fiscal_mit."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmit_api_envio_arquivos_mensagem"
MODULO = "fiscal_mit"
ENTIDADES = ['efmit_api_envio_arquivos_mensagem']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

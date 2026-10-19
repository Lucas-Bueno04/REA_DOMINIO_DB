# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geconfiguracao_envio_email (Tabela para definição do tipo da configuração do envio de email) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geconfiguracao_envio_email"
MODULO = "geral_outros"
ENTIDADES = ['geconfiguracao_envio_email']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

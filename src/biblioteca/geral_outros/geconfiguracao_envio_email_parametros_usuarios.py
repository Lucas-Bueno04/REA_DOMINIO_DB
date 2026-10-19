# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geconfiguracao_envio_email_parametros_usuarios (Tabela de relação dos usuários com a configuração de parâmetros) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geconfiguracao_envio_email_parametros_usuarios"
MODULO = "geral_outros"
ENTIDADES = ['geconfiguracao_envio_email_parametros_usuarios']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

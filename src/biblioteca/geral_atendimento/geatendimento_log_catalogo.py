# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_log_catalogo (Log dos Catalogos de NF-e retornados do servidor.) - módulo geral_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_log_catalogo"
MODULO = "geral_atendimento"
ENTIDADES = ['geatendimento_log_catalogo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

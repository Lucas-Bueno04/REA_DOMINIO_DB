# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_mimetype (Tipos de arquivos que são enviados para ASIS) - módulo geral_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_mimetype"
MODULO = "geral_atendimento"
ENTIDADES = ['geatendimento_mimetype']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

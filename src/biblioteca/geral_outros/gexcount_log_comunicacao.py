# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gexcount_log_comunicacao (XCOUNT - Log de Comunicação) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gexcount_log_comunicacao"
MODULO = "geral_outros"
ENTIDADES = ['gexcount_log_comunicacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

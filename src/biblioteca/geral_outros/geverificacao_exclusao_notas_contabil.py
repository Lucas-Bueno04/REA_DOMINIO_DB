# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geverificacao_exclusao_notas_contabil (Tabela com configurações do OnBalance.) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geverificacao_exclusao_notas_contabil"
MODULO = "geral_outros"
ENTIDADES = ['geverificacao_exclusao_notas_contabil']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

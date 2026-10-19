# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foafastamentos_competencia (Situação mensal do empregado (trabalhando, férias, afastado...)) - módulo folha_historico."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foafastamentos_competencia"
MODULO = "folha_historico"
ENTIDADES = ['situacao_mensal_empregado']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

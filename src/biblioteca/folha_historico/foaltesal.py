# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foaltesal (Alterações salariais do empregado) - módulo folha_historico."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foaltesal"
MODULO = "folha_historico"
ENTIDADES = ['alteracao_salarial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

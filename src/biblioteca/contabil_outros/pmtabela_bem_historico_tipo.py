# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmtabela_bem_historico_tipo (Tabela Tipo para Históricos do Bem) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmtabela_bem_historico_tipo"
MODULO = "contabil_outros"
ENTIDADES = ['pmtabela_bem_historico_tipo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

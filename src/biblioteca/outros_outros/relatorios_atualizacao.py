# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela relatorios_atualizacao (CONTROLE DE ATUALIZACO DE RELATORIOS DO GERADOR) - módulo outros_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "relatorios_atualizacao"
MODULO = "outros_outros"
ENTIDADES = ['relatorios_atualizacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

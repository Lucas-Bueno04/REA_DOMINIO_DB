# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lairadex (Adicoes e Exclusoes do IR - Cadastro) - módulo contabil_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lairadex"
MODULO = "contabil_nucleo"
ENTIDADES = ['lairadex']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

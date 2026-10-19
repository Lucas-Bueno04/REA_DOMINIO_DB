# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctgrupo_ebitda (Estrutura EBITDA) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctgrupo_ebitda"
MODULO = "contabil_outros"
ENTIDADES = ['ctgrupo_ebitda']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

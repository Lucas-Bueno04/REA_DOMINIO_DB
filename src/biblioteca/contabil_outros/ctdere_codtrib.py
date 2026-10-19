# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctdere_codtrib (Catalogo oficial de codigos de tributacao (codTrib) da Tabela 11 da DeRE) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctdere_codtrib"
MODULO = "contabil_outros"
ENTIDADES = ['ctdere_codtrib']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctdirigentes_conselheiros (Dirigentes e Conselheiros) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctdirigentes_conselheiros"
MODULO = "contabil_outros"
ENTIDADES = ['ctdirigentes_conselheiros']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

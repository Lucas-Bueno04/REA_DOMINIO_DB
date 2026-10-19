# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctatendimento_lancto_catalogo (Catálogo de lancamentos - Domínio Atendimento) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctatendimento_lancto_catalogo"
MODULO = "contabil_outros"
ENTIDADES = ['ctatendimento_lancto_catalogo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

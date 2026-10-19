# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctdirigentes_conselheiros_config (Configuracao de dirigentes e conselheiros) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctdirigentes_conselheiros_config"
MODULO = "contabil_outros"
ENTIDADES = ['ctdirigentes_conselheiros_config']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

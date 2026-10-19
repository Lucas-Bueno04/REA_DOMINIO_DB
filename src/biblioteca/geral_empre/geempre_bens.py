# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geempre_bens (Empresa - Bens) - módulo geral_empre."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geempre_bens"
MODULO = "geral_empre"
ENTIDADES = ['geempre_bens']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

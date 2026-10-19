# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geempre_informacoes (Empresa - Outras Informacoes) - módulo geral_empre."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geempre_informacoes"
MODULO = "geral_empre"
ENTIDADES = ['geempre_informacoes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

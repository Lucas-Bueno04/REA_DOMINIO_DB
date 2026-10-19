# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geempresa_bloqueio_historico (Empresas bloqueadas - Históricos) - módulo geral_empresa."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geempresa_bloqueio_historico"
MODULO = "geral_empresa"
ENTIDADES = ['geempresa_bloqueio_historico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

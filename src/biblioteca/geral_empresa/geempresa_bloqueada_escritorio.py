# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geempresa_bloqueada_escritorio (Empresas bloqueadas - Escritório que bloqueou) - módulo geral_empresa."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geempresa_bloqueada_escritorio"
MODULO = "geral_empresa"
ENTIDADES = ['geempresa_bloqueada_escritorio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

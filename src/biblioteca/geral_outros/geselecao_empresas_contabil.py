# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geselecao_empresas_contabil (Filtros de seleção de empresas) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geselecao_empresas_contabil"
MODULO = "geral_outros"
ENTIDADES = ['geselecao_empresas_contabil']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

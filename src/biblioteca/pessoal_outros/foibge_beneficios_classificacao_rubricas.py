# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foibge_beneficios_classificacao_rubricas (Configuração de rúbricas para lançamento do IBGE) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foibge_beneficios_classificacao_rubricas"
MODULO = "pessoal_outros"
ENTIDADES = ['foibge_beneficios_classificacao_rubricas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

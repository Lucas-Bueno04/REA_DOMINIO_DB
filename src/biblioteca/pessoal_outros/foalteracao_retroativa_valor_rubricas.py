# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foalteracao_retroativa_valor_rubricas (Alteração retroativa de valor das rubricas.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foalteracao_retroativa_valor_rubricas"
MODULO = "pessoal_outros"
ENTIDADES = ['foalteracao_retroativa_valor_rubricas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

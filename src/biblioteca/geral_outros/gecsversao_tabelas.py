# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecsversao_tabelas (Versão das tabelas da Central de Soluções) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecsversao_tabelas"
MODULO = "geral_outros"
ENTIDADES = ['gecsversao_tabelas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela getipo_selecao_selecionar (Tipos de seleção - selecionar) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "getipo_selecao_selecionar"
MODULO = "geral_outros"
ENTIDADES = ['getipo_selecao_selecionar']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

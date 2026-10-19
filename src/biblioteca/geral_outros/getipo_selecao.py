# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela getipo_selecao (Tipos de seleção) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "getipo_selecao"
MODULO = "geral_outros"
ENTIDADES = ['getipo_selecao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

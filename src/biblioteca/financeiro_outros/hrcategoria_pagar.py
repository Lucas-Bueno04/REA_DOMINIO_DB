# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrcategoria_pagar (Categorias de contas a receber) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrcategoria_pagar"
MODULO = "financeiro_outros"
ENTIDADES = ['hrcategoria_pagar']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

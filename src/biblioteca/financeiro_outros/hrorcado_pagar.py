# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrorcado_pagar (Lancamentos orcados de contas a pagar) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrorcado_pagar"
MODULO = "financeiro_outros"
ENTIDADES = ['hrorcado_pagar']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

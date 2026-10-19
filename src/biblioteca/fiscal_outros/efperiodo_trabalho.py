# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efperiodo_trabalho (Período de Trabalho) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efperiodo_trabalho"
MODULO = "fiscal_outros"
ENTIDADES = ['efperiodo_trabalho']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

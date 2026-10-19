# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efparcelar_imposto (Parcelar Imposto) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efparcelar_imposto"
MODULO = "fiscal_outros"
ENTIDADES = ['efparcelar_imposto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

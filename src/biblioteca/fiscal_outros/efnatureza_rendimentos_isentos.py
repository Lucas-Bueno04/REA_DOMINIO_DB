# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efnatureza_rendimentos_isentos (Natureza de rendimento - isentos) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efnatureza_rendimentos_isentos"
MODULO = "fiscal_outros"
ENTIDADES = ['efnatureza_rendimentos_isentos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

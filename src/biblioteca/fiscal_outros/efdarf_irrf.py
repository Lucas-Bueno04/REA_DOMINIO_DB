# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efdarf_irrf (DARF IRRF Por Nota) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efdarf_irrf"
MODULO = "fiscal_outros"
ENTIDADES = ['efdarf_irrf']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

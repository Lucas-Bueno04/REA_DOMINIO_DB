# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efregerando_lanctos_contabeis (Regerar Lançamentos Contábeis) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efregerando_lanctos_contabeis"
MODULO = "fiscal_outros"
ENTIDADES = ['efregerando_lanctos_contabeis']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

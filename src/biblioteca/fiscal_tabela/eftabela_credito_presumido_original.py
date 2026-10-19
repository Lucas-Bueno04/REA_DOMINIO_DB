# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_credito_presumido_original (Credito Presumido Importacao - Original) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_credito_presumido_original"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_credito_presumido_original']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

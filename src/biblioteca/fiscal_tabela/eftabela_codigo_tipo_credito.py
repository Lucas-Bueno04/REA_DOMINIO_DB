# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_codigo_tipo_credito (Tabela Codigo de Tipo de Credito) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_codigo_tipo_credito"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_codigo_tipo_credito']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

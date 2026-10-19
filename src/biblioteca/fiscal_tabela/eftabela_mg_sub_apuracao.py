# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_mg_sub_apuracao (Tabela de incentivos do Crédito Estímulo MG) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_mg_sub_apuracao"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_mg_sub_apuracao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

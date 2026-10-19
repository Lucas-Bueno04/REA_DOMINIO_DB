# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_mg_incentivo_ret_faixas (Tabela de incentivos do Crédito Estímulo MG - Faixas) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_mg_incentivo_ret_faixas"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_mg_incentivo_ret_faixas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

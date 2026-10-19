# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_classificacao_tributaria_is (Tabela Classificacao de classificação tributaria do imposto seletivo - IS) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_classificacao_tributaria_is"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_classificacao_tributaria_is']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

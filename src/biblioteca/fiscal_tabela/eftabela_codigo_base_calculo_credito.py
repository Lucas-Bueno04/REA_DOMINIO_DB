# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_codigo_base_calculo_credito (Tabela Codigo de Base de Calculo do Credito) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_codigo_base_calculo_credito"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_codigo_base_calculo_credito']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

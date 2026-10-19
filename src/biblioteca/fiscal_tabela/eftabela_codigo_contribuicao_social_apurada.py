# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_codigo_contribuicao_social_apurada (Tabela Codigo de Contribuicao Social Apurada) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_codigo_contribuicao_social_apurada"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_codigo_contribuicao_social_apurada']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

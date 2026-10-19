# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gesieg_dados_sessao_company (Dados da sessão referentes à SIEG) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gesieg_dados_sessao_company"
MODULO = "geral_outros"
ENTIDADES = ['gesieg_dados_sessao_company']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

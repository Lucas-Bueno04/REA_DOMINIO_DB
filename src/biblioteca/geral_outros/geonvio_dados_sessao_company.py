# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geonvio_dados_sessao_company (Dados de sessão do company referentes à Company) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geonvio_dados_sessao_company"
MODULO = "geral_outros"
ENTIDADES = ['geonvio_dados_sessao_company']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

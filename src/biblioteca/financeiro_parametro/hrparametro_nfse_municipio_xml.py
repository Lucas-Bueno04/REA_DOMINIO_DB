# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrparametro_nfse_municipio_xml (Parâmetro Honorarios - Tabela utilizada para montar o XML de envio de RPS para municípios específicos) - módulo financeiro_parametro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrparametro_nfse_municipio_xml"
MODULO = "financeiro_parametro"
ENTIDADES = ['hrparametro_nfse_municipio_xml']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geconsulta_web_service_portal_federal_versao (Consulta NF-e Webservice Portal Federal - Versão) - módulo geral_consulta."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geconsulta_web_service_portal_federal_versao"
MODULO = "geral_consulta"
ENTIDADES = ['geconsulta_web_service_portal_federal_versao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

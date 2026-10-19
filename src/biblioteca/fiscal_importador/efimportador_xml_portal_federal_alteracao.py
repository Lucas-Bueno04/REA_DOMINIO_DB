# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_xml_portal_federal_alteracao (Configuração de Importação do Download do XML do Portal Federal - Possui alteração) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_xml_portal_federal_alteracao"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_xml_portal_federal_alteracao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

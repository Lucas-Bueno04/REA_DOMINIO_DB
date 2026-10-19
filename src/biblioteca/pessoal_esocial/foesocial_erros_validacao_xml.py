# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_erros_validacao_xml (Erros de validação do XML (XSD)) - módulo pessoal_esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_erros_validacao_xml"
MODULO = "pessoal_esocial"
ENTIDADES = ['foesocial_erros_validacao_xml']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

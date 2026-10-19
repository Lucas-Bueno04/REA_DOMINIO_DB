# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efd_reinf_envio_arquivos_xml (EFD-Reinf - Envio dos Arquivos - XML) - módulo fiscal_d."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efd_reinf_envio_arquivos_xml"
MODULO = "fiscal_d"
ENTIDADES = ['efd_reinf_envio_arquivos_xml']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fodarf_dctfweb_api_bilhetagem (DARF DCTFWeb Api - Envio dos Arquivos - Bilhetagem de custos) - módulo pessoal_darf."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fodarf_dctfweb_api_bilhetagem"
MODULO = "pessoal_darf"
ENTIDADES = ['fodarf_dctfweb_api_bilhetagem']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

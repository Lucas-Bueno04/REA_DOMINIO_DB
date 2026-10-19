# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efdefis_api_bilhetagem (DEFIS Api - Envio dos Arquivos - Bilhetagem de custos) - módulo fiscal_defis."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efdefis_api_bilhetagem"
MODULO = "fiscal_defis"
ENTIDADES = ['efdefis_api_bilhetagem']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

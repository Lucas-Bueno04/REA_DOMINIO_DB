# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efdarj_envio_arquivos (DARJ - Envio dos Arquivos) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efdarj_envio_arquivos"
MODULO = "fiscal_outros"
ENTIDADES = ['efdarj_envio_arquivos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

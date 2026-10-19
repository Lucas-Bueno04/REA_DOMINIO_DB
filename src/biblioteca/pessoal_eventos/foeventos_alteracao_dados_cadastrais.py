# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foeventos_alteracao_dados_cadastrais (Alteração de dados cadastrais do histórico do cadastro de rubricas) - módulo pessoal_eventos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foeventos_alteracao_dados_cadastrais"
MODULO = "pessoal_eventos"
ENTIDADES = ['foeventos_alteracao_dados_cadastrais']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

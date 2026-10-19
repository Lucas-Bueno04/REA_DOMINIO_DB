# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gever_executado (Arquivos .ver executados na versão) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gever_executado"
MODULO = "geral_outros"
ENTIDADES = ['gever_executado']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

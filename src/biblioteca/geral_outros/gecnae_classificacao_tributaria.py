# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecnae_classificacao_tributaria (Classificação de códigos CNAE quanto à elegibilidade ao Simples Nacional: impeditivos, híbridos ou fator R) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecnae_classificacao_tributaria"
MODULO = "geral_outros"
ENTIDADES = ['gecnae_classificacao_tributaria']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

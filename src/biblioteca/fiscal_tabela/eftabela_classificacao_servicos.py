# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_classificacao_servicos (Tabela Classificacao de Itens dos Servicos de Comunicacao e Telecomunicacao) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_classificacao_servicos"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_classificacao_servicos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

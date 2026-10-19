# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efespecificacao_am (Lista de especificacoes do detalhamento de ajuste - AM) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efespecificacao_am"
MODULO = "fiscal_outros"
ENTIDADES = ['efespecificacao_am']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

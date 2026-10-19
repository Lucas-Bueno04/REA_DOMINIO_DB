# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lroperacao_receita_conta_contabil (Contas contábeis da operação de receita) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lroperacao_receita_conta_contabil"
MODULO = "contabil_outros"
ENTIDADES = ['lroperacao_receita_conta_contabil']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

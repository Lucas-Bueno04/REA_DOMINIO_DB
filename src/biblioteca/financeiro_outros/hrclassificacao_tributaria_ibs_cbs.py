# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrclassificacao_tributaria_ibs_cbs (Classificações Tributárias IBS e CBS) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrclassificacao_tributaria_ibs_cbs"
MODULO = "financeiro_outros"
ENTIDADES = ['hrclassificacao_tributaria_ibs_cbs']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

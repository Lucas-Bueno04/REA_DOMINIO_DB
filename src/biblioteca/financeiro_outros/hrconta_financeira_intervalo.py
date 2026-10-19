# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrconta_financeira_intervalo (Conta financeira - intervalo de numeracao) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrconta_financeira_intervalo"
MODULO = "financeiro_outros"
ENTIDADES = ['hrconta_financeira_intervalo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

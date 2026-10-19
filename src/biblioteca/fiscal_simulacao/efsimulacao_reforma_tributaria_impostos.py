# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsimulacao_reforma_tributaria_impostos (Simulador Reforma Tributaria - Impostos Apuracao) - módulo fiscal_simulacao."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsimulacao_reforma_tributaria_impostos"
MODULO = "fiscal_simulacao"
ENTIDADES = ['efsimulacao_reforma_tributaria_impostos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

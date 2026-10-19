# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrconta_corrente_escritorio_impostos (Tabela de detalhamento de imposto/encargo para cada movimentacao financeira) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrconta_corrente_escritorio_impostos"
MODULO = "financeiro_outros"
ENTIDADES = ['hrconta_corrente_escritorio_impostos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

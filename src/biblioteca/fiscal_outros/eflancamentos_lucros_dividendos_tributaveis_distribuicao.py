# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eflancamentos_lucros_dividendos_tributaveis_distribuicao (Distribuição de lucros e dividendos tributáveis) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eflancamentos_lucros_dividendos_tributaveis_distribuicao"
MODULO = "fiscal_outros"
ENTIDADES = ['eflancamentos_lucros_dividendos_tributaveis_distribuicao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

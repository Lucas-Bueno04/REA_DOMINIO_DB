# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eflucros_dividendos_tributaveis_distribuicao_contas_param (Distribuição de lucros e dividendos tributáveis - Contas parâmetros) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eflucros_dividendos_tributaveis_distribuicao_contas_param"
MODULO = "fiscal_outros"
ENTIDADES = ['eflucros_dividendos_tributaveis_distribuicao_contas_param']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

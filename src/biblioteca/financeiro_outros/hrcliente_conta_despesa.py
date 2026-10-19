# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrcliente_conta_despesa (Clientes Fixos e Eventuais - Contas de Despesas) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrcliente_conta_despesa"
MODULO = "financeiro_outros"
ENTIDADES = ['hrcliente_conta_despesa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

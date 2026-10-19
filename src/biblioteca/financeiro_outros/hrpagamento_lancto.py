# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrpagamento_lancto (Pagamentos de contas a pagar X Lancamentos Contabeis) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrpagamento_lancto"
MODULO = "financeiro_outros"
ENTIDADES = ['hrpagamento_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrrecebimento_lancto (Recebimento de contas a receber X Lancamentos Contabeis) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrrecebimento_lancto"
MODULO = "financeiro_outros"
ENTIDADES = ['hrrecebimento_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

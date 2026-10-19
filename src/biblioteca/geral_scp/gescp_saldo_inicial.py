# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gescp_saldo_inicial (Sociedade em Conta de Participação - SCP - Saldo Inicial) - módulo geral_scp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gescp_saldo_inicial"
MODULO = "geral_scp"
ENTIDADES = ['gescp_saldo_inicial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcontas_sped_ecf_sistema_financeiro (Plano de contas SPED ECF Sistema Financeiro) - módulo contabil_contas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcontas_sped_ecf_sistema_financeiro"
MODULO = "contabil_contas"
ENTIDADES = ['ctcontas_sped_ecf_sistema_financeiro']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

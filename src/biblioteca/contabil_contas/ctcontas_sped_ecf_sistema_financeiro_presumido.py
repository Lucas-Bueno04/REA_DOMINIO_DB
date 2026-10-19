# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcontas_sped_ecf_sistema_financeiro_presumido (Plano de contas SPED ECF Pessoa Jurídica Financeira - Lucro Presumido) - módulo contabil_contas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcontas_sped_ecf_sistema_financeiro_presumido"
MODULO = "contabil_contas"
ENTIDADES = ['ctcontas_sped_ecf_sistema_financeiro_presumido']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

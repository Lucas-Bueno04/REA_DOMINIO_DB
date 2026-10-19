# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcontas_sped_ecf_geral_ref_sa_scp (Plano de contas SPED ECF Geral Referencial - Saldo anterior por SCP) - módulo contabil_contas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcontas_sped_ecf_geral_ref_sa_scp"
MODULO = "contabil_contas"
ENTIDADES = ['ctcontas_sped_ecf_geral_ref_sa_scp']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

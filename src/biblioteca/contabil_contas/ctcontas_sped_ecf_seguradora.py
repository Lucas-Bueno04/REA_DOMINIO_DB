# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcontas_sped_ecf_seguradora (Plano de contas SPED ECF Seguradoras ou Entidades Abertas de Previdência Complementar) - módulo contabil_contas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcontas_sped_ecf_seguradora"
MODULO = "contabil_contas"
ENTIDADES = ['ctcontas_sped_ecf_seguradora']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

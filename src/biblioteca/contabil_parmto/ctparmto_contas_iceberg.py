# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctparmto_contas_iceberg (Parâmetrização de contas Contabilidade Digital) - módulo contabil_parmto."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctparmto_contas_iceberg"
MODULO = "contabil_parmto"
ENTIDADES = ['ctparmto_contas_iceberg']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctparmto_sped_vigencia (Parâmetros Contabilidade - Vigência da guia Dados SPED) - módulo contabil_parmto."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctparmto_sped_vigencia"
MODULO = "contabil_parmto"
ENTIDADES = ['ctparmto_sped_vigencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

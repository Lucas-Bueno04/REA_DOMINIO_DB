# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctparmto_dere_vigencia (Parametros Contabilidade - Vigencia da guia Informativos/DeRE) - módulo contabil_parmto."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctparmto_dere_vigencia"
MODULO = "contabil_parmto"
ENTIDADES = ['ctparmto_dere_vigencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

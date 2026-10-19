# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcontacaixa (Parametros - Cadastro - Contas caixa) - módulo contabil_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcontacaixa"
MODULO = "contabil_nucleo"
ENTIDADES = ['ctcontacaixa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

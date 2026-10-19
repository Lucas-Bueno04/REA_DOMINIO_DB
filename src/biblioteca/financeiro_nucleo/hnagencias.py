# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hnagencias (Agencias Bancarias - Cadastro) - módulo financeiro_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hnagencias"
MODULO = "financeiro_nucleo"
ENTIDADES = ['hnagencias']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

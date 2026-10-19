# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabelamuni_itens (Tabelas Municipais - Cadastro - Itens) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabelamuni_itens"
MODULO = "fiscal_outros"
ENTIDADES = ['eftabelamuni_itens']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

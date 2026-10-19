# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efecf_reducao_z_estoque (ECF - Dados da redução Z - Estoque) - módulo fiscal_ecf."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efecf_reducao_z_estoque"
MODULO = "fiscal_ecf"
ENTIDADES = ['efecf_reducao_z_estoque']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

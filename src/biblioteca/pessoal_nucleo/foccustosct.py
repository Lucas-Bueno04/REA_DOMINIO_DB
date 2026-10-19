# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foccustosct (Cadastro - Relacionamento do centro de custos da folha com a contabilidade) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foccustosct"
MODULO = "pessoal_nucleo"
ENTIDADES = ['foccustosct']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela rgtabela_codigo_receita (Codigo da Receita) - módulo societario_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "rgtabela_codigo_receita"
MODULO = "societario_outros"
ENTIDADES = ['rgtabela_codigo_receita']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

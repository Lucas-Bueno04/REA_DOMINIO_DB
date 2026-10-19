# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gedados_reforma_tributaria (Dados da Reforma Tributária - Acesso ao módulo) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gedados_reforma_tributaria"
MODULO = "geral_outros"
ENTIDADES = ['gedados_reforma_tributaria']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

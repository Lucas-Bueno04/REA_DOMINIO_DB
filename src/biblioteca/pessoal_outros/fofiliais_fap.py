# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fofiliais_fap (Informações do FAP para a filial a partir de 01/2016.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fofiliais_fap"
MODULO = "pessoal_outros"
ENTIDADES = ['fofiliais_fap']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

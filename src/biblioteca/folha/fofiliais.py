# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fofiliais (Filiais (folha)) - módulo folha."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fofiliais"
MODULO = "folha"
ENTIDADES = ['filial_folha']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

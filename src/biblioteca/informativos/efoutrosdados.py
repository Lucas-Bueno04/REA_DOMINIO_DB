# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoutrosdados (Informativos preparados por empresa e competência) - módulo informativos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoutrosdados"
MODULO = "informativos"
ENTIDADES = ['informativo_empresa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

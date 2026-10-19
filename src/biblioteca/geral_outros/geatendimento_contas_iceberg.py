# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_contas_iceberg (Contas financeiras Iceberg) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_contas_iceberg"
MODULO = "geral_outros"
ENTIDADES = ['geatendimento_contas_iceberg']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

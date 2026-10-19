# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecheckpoint_incentivos_fiscais_cnae (Codigo de atividade economica) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecheckpoint_incentivos_fiscais_cnae"
MODULO = "geral_outros"
ENTIDADES = ['gecheckpoint_incentivos_fiscais_cnae']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecampo_cabecalho_auditor (Cabeçalho Auditor Digital) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecampo_cabecalho_auditor"
MODULO = "geral_outros"
ENTIDADES = ['gecampo_cabecalho_auditor']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

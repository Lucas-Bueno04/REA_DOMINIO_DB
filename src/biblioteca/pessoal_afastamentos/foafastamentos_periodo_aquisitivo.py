# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foafastamentos_periodo_aquisitivo (AFASTAMENTOS SEPARADOS POR PERIODO AQUISITIVO) - módulo pessoal_afastamentos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foafastamentos_periodo_aquisitivo"
MODULO = "pessoal_afastamentos"
ENTIDADES = ['foafastamentos_periodo_aquisitivo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

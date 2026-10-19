# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foconvenios_terceiros (Tabela de convênios de terceiros.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foconvenios_terceiros"
MODULO = "pessoal_outros"
ENTIDADES = ['foconvenios_terceiros']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

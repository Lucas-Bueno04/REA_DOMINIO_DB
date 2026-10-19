# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foadvertencia_suspensao (Cadastro de advertências e suspensões de empregados) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foadvertencia_suspensao"
MODULO = "pessoal_outros"
ENTIDADES = ['foadvertencia_suspensao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

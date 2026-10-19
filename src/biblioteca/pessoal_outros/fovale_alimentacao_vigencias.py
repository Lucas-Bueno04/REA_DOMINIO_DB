# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fovale_alimentacao_vigencias (Vale alimentação - Vigências) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fovale_alimentacao_vigencias"
MODULO = "pessoal_outros"
ENTIDADES = ['fovale_alimentacao_vigencias']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

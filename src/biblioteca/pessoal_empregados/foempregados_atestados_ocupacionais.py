# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foempregados_atestados_ocupacionais (Cadastro de Empregados - Atestados Ocupacionais) - módulo pessoal_empregados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foempregados_atestados_ocupacionais"
MODULO = "pessoal_empregados"
ENTIDADES = ['foempregados_atestados_ocupacionais']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

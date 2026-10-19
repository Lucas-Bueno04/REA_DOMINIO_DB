# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foempregados_atestados_ocupacionais_exames (Cadastro de Empregados - Atestados Ocupacionais - Exames) - módulo pessoal_empregados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foempregados_atestados_ocupacionais_exames"
MODULO = "pessoal_empregados"
ENTIDADES = ['foempregados_atestados_ocupacionais_exames']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

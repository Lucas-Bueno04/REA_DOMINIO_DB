# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foempregados_estabilidade (Estabilidades do empregado.) - módulo pessoal_empregados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foempregados_estabilidade"
MODULO = "pessoal_empregados"
ENTIDADES = ['foempregados_estabilidade']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

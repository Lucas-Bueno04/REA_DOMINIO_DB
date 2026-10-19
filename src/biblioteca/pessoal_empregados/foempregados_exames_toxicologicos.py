# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foempregados_exames_toxicologicos (Exames toxicológicos dos empregados) - módulo pessoal_empregados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foempregados_exames_toxicologicos"
MODULO = "pessoal_empregados"
ENTIDADES = ['foempregados_exames_toxicologicos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

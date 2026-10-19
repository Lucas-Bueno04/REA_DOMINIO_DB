# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foempregados_esocial_domestico (Cadastro de Empregados Domésticos - eSocial Doméstico) - módulo pessoal_empregados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foempregados_esocial_domestico"
MODULO = "pessoal_empregados"
ENTIDADES = ['foempregados_esocial_domestico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

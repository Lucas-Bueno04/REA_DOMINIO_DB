# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foencargos_emprestimo_credito_trabalhador (Encargos do empréstimo do crédito do trabalhador da competência) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foencargos_emprestimo_credito_trabalhador"
MODULO = "pessoal_outros"
ENTIDADES = ['foencargos_emprestimo_credito_trabalhador']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

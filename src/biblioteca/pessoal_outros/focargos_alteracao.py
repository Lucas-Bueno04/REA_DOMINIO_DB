# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focargos_alteracao (Tabela de alterações.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focargos_alteracao"
MODULO = "pessoal_outros"
ENTIDADES = ['focargos_alteracao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

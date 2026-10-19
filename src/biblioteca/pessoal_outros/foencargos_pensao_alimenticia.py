# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foencargos_pensao_alimenticia (Encargo de pensão alimentícia.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foencargos_pensao_alimenticia"
MODULO = "pessoal_outros"
ENTIDADES = ['foencargos_pensao_alimenticia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

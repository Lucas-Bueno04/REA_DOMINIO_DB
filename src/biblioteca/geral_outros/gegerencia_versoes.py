# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gegerencia_versoes (Gerencia Versoes de Sistema) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gegerencia_versoes"
MODULO = "geral_outros"
ENTIDADES = ['gegerencia_versoes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

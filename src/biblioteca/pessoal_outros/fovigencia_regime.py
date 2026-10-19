# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fovigencia_regime (Tabela de vigências do regime da empresa) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fovigencia_regime"
MODULO = "pessoal_outros"
ENTIDADES = ['fovigencia_regime']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

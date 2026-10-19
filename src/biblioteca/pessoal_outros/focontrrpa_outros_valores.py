# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focontrrpa_outros_valores (Outros valores RPA) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focontrrpa_outros_valores"
MODULO = "pessoal_outros"
ENTIDADES = ['focontrrpa_outros_valores']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

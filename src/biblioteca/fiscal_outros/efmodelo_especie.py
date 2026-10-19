# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmodelo_especie (Modelos das espécies) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmodelo_especie"
MODULO = "fiscal_outros"
ENTIDADES = ['efmodelo_especie']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

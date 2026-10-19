# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efespecies (Espécies de documento fiscal) - módulo fiscal."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efespecies"
MODULO = "fiscal"
ENTIDADES = ['especie_documento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

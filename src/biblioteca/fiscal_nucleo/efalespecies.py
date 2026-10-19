# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efalespecies (Especies - Cadastro - AL) - módulo fiscal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efalespecies"
MODULO = "fiscal_nucleo"
ENTIDADES = ['efalespecies']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efceespecies (Especies - Cadastro - CE) - módulo fiscal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efceespecies"
MODULO = "fiscal_nucleo"
ENTIDADES = ['efceespecies']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

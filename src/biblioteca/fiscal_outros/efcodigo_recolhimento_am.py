# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcodigo_recolhimento_am (Codigos de recolhimento do ICMS - AM) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcodigo_recolhimento_am"
MODULO = "fiscal_outros"
ENTIDADES = ['efcodigo_recolhimento_am']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcnae_fortaleza (Tabela do CNAE Fortaleza) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcnae_fortaleza"
MODULO = "fiscal_outros"
ENTIDADES = ['efcnae_fortaleza']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

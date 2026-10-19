# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efservicospag_lancto (Baixas de servicos X Lancamentos contabeis) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efservicospag_lancto"
MODULO = "fiscal_outros"
ENTIDADES = ['efservicospag_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

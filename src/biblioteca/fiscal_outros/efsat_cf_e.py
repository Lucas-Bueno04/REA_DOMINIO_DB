# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsat_cf_e (SAT CF-e) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsat_cf_e"
MODULO = "fiscal_outros"
ENTIDADES = ['efsat_cf_e']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

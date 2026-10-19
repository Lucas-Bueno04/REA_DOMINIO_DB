# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradas_efd_reinf (Notas Fiscais de Entrada - EFD Reinf) - módulo fiscal_entradas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradas_efd_reinf"
MODULO = "fiscal_entradas"
ENTIDADES = ['efentradas_efd_reinf']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

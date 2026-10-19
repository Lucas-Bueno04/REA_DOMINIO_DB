# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradas_difal_nc (Notas Fiscais de Entrada - DIFAL NC) - módulo fiscal_entradas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradas_difal_nc"
MODULO = "fiscal_entradas"
ENTIDADES = ['efentradas_difal_nc']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

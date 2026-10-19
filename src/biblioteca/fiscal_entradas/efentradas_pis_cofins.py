# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradas_pis_cofins (Notas Fiscais de Entrada - PIS/COFINS) - módulo fiscal_entradas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradas_pis_cofins"
MODULO = "fiscal_entradas"
ENTIDADES = ['efentradas_pis_cofins']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

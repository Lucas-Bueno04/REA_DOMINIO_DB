# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradas_nota_devolvida_csoc_irpj (Notas Fiscais de Entrada - Complementar - Geral - Nota Devolvida - CSOC/IRPJ) - módulo fiscal_entradas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradas_nota_devolvida_csoc_irpj"
MODULO = "fiscal_entradas"
ENTIDADES = ['efentradas_nota_devolvida_csoc_irpj']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

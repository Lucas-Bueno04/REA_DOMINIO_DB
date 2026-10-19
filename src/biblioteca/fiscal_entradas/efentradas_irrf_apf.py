# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradas_irrf_apf (Notas Fiscais de Entrada - Dados IRRF) - módulo fiscal_entradas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradas_irrf_apf"
MODULO = "fiscal_entradas"
ENTIDADES = ['efentradas_irrf_apf']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradas_detalhamento_mg (Notas Fiscais de Entradas - Detalhamentos - MG) - módulo fiscal_entradas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradas_detalhamento_mg"
MODULO = "fiscal_entradas"
ENTIDADES = ['efentradas_detalhamento_mg']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradas_inss_rb (Notas Fiscais de Entradas - INSS Receita Bruta) - módulo fiscal_entradas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradas_inss_rb"
MODULO = "fiscal_entradas"
ENTIDADES = ['efentradas_inss_rb']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

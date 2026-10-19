# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradas_estadual_pe (Notas Fiscais de Entradas - Dados estaduais - PE) - módulo fiscal_entradas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradas_estadual_pe"
MODULO = "fiscal_entradas"
ENTIDADES = ['efentradas_estadual_pe']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

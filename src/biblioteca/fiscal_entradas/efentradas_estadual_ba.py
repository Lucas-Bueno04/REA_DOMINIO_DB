# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradas_estadual_ba (Notas Fiscais de Entradas - Dados estaduais - BA) - módulo fiscal_entradas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradas_estadual_ba"
MODULO = "fiscal_entradas"
ENTIDADES = ['efentradas_estadual_ba']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

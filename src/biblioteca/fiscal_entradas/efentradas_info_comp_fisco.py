# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradas_info_comp_fisco (Notas Fiscais de Entradas - Informação complementar de interesse do fisco) - módulo fiscal_entradas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradas_info_comp_fisco"
MODULO = "fiscal_entradas"
ENTIDADES = ['efentradas_info_comp_fisco']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

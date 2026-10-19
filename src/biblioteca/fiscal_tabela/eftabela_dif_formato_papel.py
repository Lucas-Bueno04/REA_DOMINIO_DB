# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_dif_formato_papel (DIF - Papel Imune - Formato de Papel) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_dif_formato_papel"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_dif_formato_papel']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

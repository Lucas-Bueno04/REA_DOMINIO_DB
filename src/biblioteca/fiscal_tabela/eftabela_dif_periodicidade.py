# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_dif_periodicidade (DIF - Papel Imune - Periodicidades) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_dif_periodicidade"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_dif_periodicidade']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_sub_apuracoes_prodepe_pe (Tabela de Sub-Apurações PRODEPE - PE) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_sub_apuracoes_prodepe_pe"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_sub_apuracoes_prodepe_pe']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_al_quadro_iii_dac (Tabela do Quadro III do Informativo DAC - Tipo do Produto) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_al_quadro_iii_dac"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_al_quadro_iii_dac']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrcsll_real_base_negativa (Base Negativa) - módulo contabil_csll."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrcsll_real_base_negativa"
MODULO = "contabil_csll"
ENTIDADES = ['lrcsll_real_base_negativa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

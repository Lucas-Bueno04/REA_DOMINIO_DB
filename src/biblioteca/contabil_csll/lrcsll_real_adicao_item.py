# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrcsll_real_adicao_item (Lançamentos de Adições da Contribuição Social - Adições) - módulo contabil_csll."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrcsll_real_adicao_item"
MODULO = "contabil_csll"
ENTIDADES = ['lrcsll_real_adicao_item']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

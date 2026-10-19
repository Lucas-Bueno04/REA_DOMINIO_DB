# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrcsll_real_deducao (Deduções da Contribuição Social (Real)) - módulo contabil_csll."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrcsll_real_deducao"
MODULO = "contabil_csll"
ENTIDADES = ['lrcsll_real_deducao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

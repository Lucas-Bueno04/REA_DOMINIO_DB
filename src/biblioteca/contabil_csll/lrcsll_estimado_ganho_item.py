# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrcsll_estimado_ganho_item (Lançamentos de Ganhos da Contribuição Social - Ganhos) - módulo contabil_csll."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrcsll_estimado_ganho_item"
MODULO = "contabil_csll"
ENTIDADES = ['lrcsll_estimado_ganho_item']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

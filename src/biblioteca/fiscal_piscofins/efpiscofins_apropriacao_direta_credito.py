# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efpiscofins_apropriacao_direta_credito (Apropriação Direta de Créditos de PIS e COFINS - Geral) - módulo fiscal_piscofins."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efpiscofins_apropriacao_direta_credito"
MODULO = "fiscal_piscofins"
ENTIDADES = ['efpiscofins_apropriacao_direta_credito']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

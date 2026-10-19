# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoutros_creditos_piscofins_imobilizado_base_piscofins (Outros creditos PIS/COFINS - Credito sobre imobilizado - Base PIS COFINS) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoutros_creditos_piscofins_imobilizado_base_piscofins"
MODULO = "fiscal_outros"
ENTIDADES = ['efoutros_creditos_piscofins_imobilizado_base_piscofins']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoutros_creditos_piscofins_imobilizado (Outros creditos PIS/COFINS - Credito sobre imobilizado) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoutros_creditos_piscofins_imobilizado"
MODULO = "fiscal_outros"
ENTIDADES = ['efoutros_creditos_piscofins_imobilizado']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efpiscofins_outros_saldo_retencao (Saldo de Retenções PIS/COFINS/Outros Saldos de Retenções) - módulo fiscal_piscofins."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efpiscofins_outros_saldo_retencao"
MODULO = "fiscal_piscofins"
ENTIDADES = ['efpiscofins_outros_saldo_retencao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

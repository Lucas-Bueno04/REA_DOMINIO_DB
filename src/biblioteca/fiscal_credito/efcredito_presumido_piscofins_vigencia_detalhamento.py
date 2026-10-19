# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcredito_presumido_piscofins_vigencia_detalhamento (Tabela de Crédito Presumido PIS e COFINS - Relação de NCM) - módulo fiscal_credito."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcredito_presumido_piscofins_vigencia_detalhamento"
MODULO = "fiscal_credito"
ENTIDADES = ['efcredito_presumido_piscofins_vigencia_detalhamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

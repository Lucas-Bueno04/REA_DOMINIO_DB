# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efparcelamento_imposto_sn_parcela_parcelamento (Parcelamento de Impostos Simples Nacional - Parcelamento) - módulo fiscal_parcelamento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efparcelamento_imposto_sn_parcela_parcelamento"
MODULO = "fiscal_parcelamento"
ENTIDADES = ['efparcelamento_imposto_sn_parcela_parcelamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

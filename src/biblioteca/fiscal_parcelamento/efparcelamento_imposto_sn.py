# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efparcelamento_imposto_sn (Parcelamento de Impostos Simples Nacional) - módulo fiscal_parcelamento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efparcelamento_imposto_sn"
MODULO = "fiscal_parcelamento"
ENTIDADES = ['efparcelamento_imposto_sn']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

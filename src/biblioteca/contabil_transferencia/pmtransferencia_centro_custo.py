# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmtransferencia_centro_custo (Transferência de Centros de Custos) - módulo contabil_transferencia."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmtransferencia_centro_custo"
MODULO = "contabil_transferencia"
ENTIDADES = ['pmtransferencia_centro_custo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

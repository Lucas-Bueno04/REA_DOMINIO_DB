# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmtransferencia_matriz_filial (Plano de contas SPED ECF Entidades Fechadas da Previdência Comp Referencial - Saldo anterior por Centro de Custo) - módulo contabil_transferencia."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmtransferencia_matriz_filial"
MODULO = "contabil_transferencia"
ENTIDADES = ['pmtransferencia_matriz_filial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmtransferencia_matriz_filial_lancto (Transferência de bens entre matriz/filiais - Lançamentos Contábeis) - módulo contabil_transferencia."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmtransferencia_matriz_filial_lancto"
MODULO = "contabil_transferencia"
ENTIDADES = ['pmtransferencia_matriz_filial_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

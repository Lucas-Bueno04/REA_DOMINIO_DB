# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctextrato_bancario_configuracao_iceberg_detalhe (Configuração para Contabilizar Extrato Bancário Contabilidade Digital - Detalhe) - módulo contabil_extrato."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctextrato_bancario_configuracao_iceberg_detalhe"
MODULO = "contabil_extrato"
ENTIDADES = ['ctextrato_bancario_configuracao_iceberg_detalhe']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

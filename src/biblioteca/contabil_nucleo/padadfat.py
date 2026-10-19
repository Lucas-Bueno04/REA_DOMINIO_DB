# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela padadfat (Dados do Faturamento inf. no Calculo Mensal do Patrimonio) - módulo contabil_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "padadfat"
MODULO = "contabil_nucleo"
ENTIDADES = ['padadfat']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

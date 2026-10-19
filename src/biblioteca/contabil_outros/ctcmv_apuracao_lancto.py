# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcmv_apuracao_lancto (CMV - Apuração do Custo das Mercadorias Vendidas - Lançamentos Contábeis) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcmv_apuracao_lancto"
MODULO = "contabil_outros"
ENTIDADES = ['ctcmv_apuracao_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

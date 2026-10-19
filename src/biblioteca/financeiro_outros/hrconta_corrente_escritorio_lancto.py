# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrconta_corrente_escritorio_lancto (Conta corrente do escritorio X Lancamentos Contabeis) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrconta_corrente_escritorio_lancto"
MODULO = "financeiro_outros"
ENTIDADES = ['hrconta_corrente_escritorio_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

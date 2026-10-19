# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrconta_corrente_escritorio (Conta corrente do escritório) - módulo honorarios."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrconta_corrente_escritorio"
MODULO = "honorarios"
ENTIDADES = ['conta_corrente_escritorio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

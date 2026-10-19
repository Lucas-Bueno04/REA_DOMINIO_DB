# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradaspar (Parcelas das notas de entrada) - módulo fiscal."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradaspar"
MODULO = "fiscal"
ENTIDADES = ['parcela_nota_entrada']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

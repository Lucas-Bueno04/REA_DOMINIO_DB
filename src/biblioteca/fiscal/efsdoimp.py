# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp (Apuração de impostos (saldos)) - módulo fiscal."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp"
MODULO = "fiscal"
ENTIDADES = ['apuracao_imposto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

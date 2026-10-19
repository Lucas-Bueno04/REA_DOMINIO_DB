# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efajustes (Códigos de ajuste da apuração) - módulo icms."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efajustes"
MODULO = "icms"
ENTIDADES = ['ajuste_apuracao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

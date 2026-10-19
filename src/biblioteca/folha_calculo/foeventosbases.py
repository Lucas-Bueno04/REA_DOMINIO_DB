# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foeventosbases (Bases em que cada evento da folha incide) - módulo folha_calculo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foeventosbases"
MODULO = "folha_calculo"
ENTIDADES = ['incidencia_evento_folha']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

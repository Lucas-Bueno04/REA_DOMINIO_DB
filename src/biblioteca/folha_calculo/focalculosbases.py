# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focalculosbases (Bases e valores de um cálculo da folha) - módulo folha_calculo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focalculosbases"
MODULO = "folha_calculo"
ENTIDADES = ['calculo_base_folha']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

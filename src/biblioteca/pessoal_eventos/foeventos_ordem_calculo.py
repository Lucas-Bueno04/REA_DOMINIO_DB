# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foeventos_ordem_calculo (Tabela de controle da ordem de cálculo das rubricas) - módulo pessoal_eventos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foeventos_ordem_calculo"
MODULO = "pessoal_eventos"
ENTIDADES = ['foeventos_ordem_calculo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

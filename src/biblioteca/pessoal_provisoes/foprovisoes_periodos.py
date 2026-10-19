# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foprovisoes_periodos (PROVISOES CALCULADAS - PERIODOS DE FERIAS) - módulo pessoal_provisoes."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foprovisoes_periodos"
MODULO = "pessoal_provisoes"
ENTIDADES = ['foprovisoes_periodos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

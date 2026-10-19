# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fosimulacao_ferias (Simulação do cálculo de férias) - módulo pessoal_simulacao."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fosimulacao_ferias"
MODULO = "pessoal_simulacao"
ENTIDADES = ['fosimulacao_ferias']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotrocas_sindpiso (TROCAS DOS PISOS DOS SINDICATOS) - módulo pessoal_trocas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotrocas_sindpiso"
MODULO = "pessoal_trocas"
ENTIDADES = ['fotrocas_sindpiso']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

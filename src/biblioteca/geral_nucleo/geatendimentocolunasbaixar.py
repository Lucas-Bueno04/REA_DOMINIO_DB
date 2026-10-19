# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimentocolunasbaixar (Colunas utilizadas pelo Agente de Comunicação para baixar dados) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimentocolunasbaixar"
MODULO = "geral_nucleo"
ENTIDADES = ['geatendimentocolunasbaixar']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

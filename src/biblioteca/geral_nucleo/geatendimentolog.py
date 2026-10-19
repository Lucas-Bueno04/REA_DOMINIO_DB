# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimentolog (Log do envio de dados do Agente de Comunicação) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimentolog"
MODULO = "geral_nucleo"
ENTIDADES = ['geatendimentolog']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

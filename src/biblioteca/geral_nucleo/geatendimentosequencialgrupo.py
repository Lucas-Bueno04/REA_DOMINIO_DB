# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimentosequencialgrupo (Sequencial do envio de dados por grupo do Agente de Comunicação) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimentosequencialgrupo"
MODULO = "geral_nucleo"
ENTIDADES = ['geatendimentosequencialgrupo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimentoacoes (Ações a serem enviadas para o Domínio Atendimento) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimentoacoes"
MODULO = "geral_nucleo"
ENTIDADES = ['geatendimentoacoes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

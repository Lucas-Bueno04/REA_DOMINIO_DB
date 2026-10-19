# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimentogrupoexecucao (Grupos de execução do Agente de Comunicação) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimentogrupoexecucao"
MODULO = "geral_nucleo"
ENTIDADES = ['geatendimentogrupoexecucao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

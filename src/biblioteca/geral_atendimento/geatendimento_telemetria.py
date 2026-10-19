# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_telemetria (Dados de integração para telemetria) - módulo geral_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_telemetria"
MODULO = "geral_atendimento"
ENTIDADES = ['geatendimento_telemetria']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

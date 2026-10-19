# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_parar_servico (Controle de parada de serviço do Agente de Comunicação) - módulo geral_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_parar_servico"
MODULO = "geral_atendimento"
ENTIDADES = ['geatendimento_parar_servico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

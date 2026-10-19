# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_controle_requisicoes (Controle de requisições para download de notas) - módulo geral_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_controle_requisicoes"
MODULO = "geral_atendimento"
ENTIDADES = ['geatendimento_controle_requisicoes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

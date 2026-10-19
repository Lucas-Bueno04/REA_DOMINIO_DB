# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_plano_contas_contabilidade (Envio do plano de contas para a Conta Azul) - módulo geral_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_plano_contas_contabilidade"
MODULO = "geral_atendimento"
ENTIDADES = ['geatendimento_plano_contas_contabilidade']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

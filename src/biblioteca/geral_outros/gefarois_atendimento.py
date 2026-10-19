# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gefarois_atendimento (Situação dos faróis de notificações) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gefarois_atendimento"
MODULO = "geral_outros"
ENTIDADES = ['gefarois_atendimento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

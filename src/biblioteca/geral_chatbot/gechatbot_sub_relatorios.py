# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gechatbot_sub_relatorios (Relação de sub-relatórios para o Assistente Virtual) - módulo geral_chatbot."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gechatbot_sub_relatorios"
MODULO = "geral_chatbot"
ENTIDADES = ['gechatbot_sub_relatorios']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gechatbot_limpeza_dados (Controla quando deve limpar os dados referente ao chatbot quando houver cancelamento, downgrade ou cessão de direitos envolvendo FRP no Onvio Messenger) - módulo geral_chatbot."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gechatbot_limpeza_dados"
MODULO = "geral_chatbot"
ENTIDADES = ['gechatbot_limpeza_dados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

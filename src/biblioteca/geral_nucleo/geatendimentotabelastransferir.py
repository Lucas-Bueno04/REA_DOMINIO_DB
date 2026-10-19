# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimentotabelastransferir (Tabelas utilizadas pelo Agente de Comunicação para realizar o envio de dados) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimentotabelastransferir"
MODULO = "geral_nucleo"
ENTIDADES = ['geatendimentotabelastransferir']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

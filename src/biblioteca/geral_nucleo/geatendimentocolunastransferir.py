# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimentocolunastransferir (Colunas utilizadas pelo Agente de Comunicação para realizar envios de dados) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimentocolunastransferir"
MODULO = "geral_nucleo"
ENTIDADES = ['geatendimentocolunastransferir']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

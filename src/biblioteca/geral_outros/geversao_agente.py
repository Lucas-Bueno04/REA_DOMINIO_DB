# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geversao_agente (Versão do Agente de Comunicação) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geversao_agente"
MODULO = "geral_outros"
ENTIDADES = ['geversao_agente']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

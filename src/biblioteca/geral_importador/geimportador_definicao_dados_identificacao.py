# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geimportador_definicao_dados_identificacao (Identificação da definição de dados) - módulo geral_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geimportador_definicao_dados_identificacao"
MODULO = "geral_importador"
ENTIDADES = ['geimportador_definicao_dados_identificacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

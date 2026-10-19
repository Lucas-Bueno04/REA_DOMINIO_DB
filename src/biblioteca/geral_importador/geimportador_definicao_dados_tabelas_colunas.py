# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geimportador_definicao_dados_tabelas_colunas (Colunas das tabelas da definição de dados) - módulo geral_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geimportador_definicao_dados_tabelas_colunas"
MODULO = "geral_importador"
ENTIDADES = ['geimportador_definicao_dados_tabelas_colunas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

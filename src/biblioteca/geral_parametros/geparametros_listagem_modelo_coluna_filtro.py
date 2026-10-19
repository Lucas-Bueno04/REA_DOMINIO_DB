# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geparametros_listagem_modelo_coluna_filtro (Configuração dos filtros dos relatórios gerados através do botão Listagem nos cadastros) - módulo geral_parametros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geparametros_listagem_modelo_coluna_filtro"
MODULO = "geral_parametros"
ENTIDADES = ['geparametros_listagem_modelo_coluna_filtro']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

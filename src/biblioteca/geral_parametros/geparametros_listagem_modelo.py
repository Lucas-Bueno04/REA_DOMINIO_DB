# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geparametros_listagem_modelo (Configuração dos relatórios gerados através do botão Listagem nos cadastros) - módulo geral_parametros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geparametros_listagem_modelo"
MODULO = "geral_parametros"
ENTIDADES = ['geparametros_listagem_modelo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

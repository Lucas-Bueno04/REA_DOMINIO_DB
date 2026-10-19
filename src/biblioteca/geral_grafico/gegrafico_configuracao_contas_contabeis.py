# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gegrafico_configuracao_contas_contabeis (Dados dos gráficos criado pelo usuário e gráficos padrões.) - módulo geral_grafico."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gegrafico_configuracao_contas_contabeis"
MODULO = "geral_grafico"
ENTIDADES = ['gegrafico_configuracao_contas_contabeis']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

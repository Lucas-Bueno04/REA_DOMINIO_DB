# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geestacoes_moduloweb (Usuário e máquina que configurou o Domínio Atendimento para o usuário) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geestacoes_moduloweb"
MODULO = "geral_outros"
ENTIDADES = ['geestacoes_moduloweb']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

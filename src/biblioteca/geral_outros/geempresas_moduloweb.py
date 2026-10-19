# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geempresas_moduloweb (Relação de empresas que utilizam o Domínio Atendimento) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geempresas_moduloweb"
MODULO = "geral_outros"
ENTIDADES = ['geempresas_moduloweb']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

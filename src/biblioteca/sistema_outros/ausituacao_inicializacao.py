# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ausituacao_inicializacao (Tabela para sinalização da inicialização e parada da Auditoria.) - módulo sistema_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ausituacao_inicializacao"
MODULO = "sistema_outros"
ENTIDADES = ['ausituacao_inicializacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

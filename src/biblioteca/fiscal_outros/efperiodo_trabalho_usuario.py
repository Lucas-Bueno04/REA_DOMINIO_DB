# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efperiodo_trabalho_usuario (Período de Trabalho - Usuário) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efperiodo_trabalho_usuario"
MODULO = "fiscal_outros"
ENTIDADES = ['efperiodo_trabalho_usuario']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

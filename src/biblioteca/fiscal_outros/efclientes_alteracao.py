# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efclientes_alteracao (Clientes - Alteracoes - Cadastro) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efclientes_alteracao"
MODULO = "fiscal_outros"
ENTIDADES = ['efclientes_alteracao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

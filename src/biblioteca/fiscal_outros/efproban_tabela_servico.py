# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efproban_tabela_servico (PROBAN - Tabela de serviços) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efproban_tabela_servico"
MODULO = "fiscal_outros"
ENTIDADES = ['efproban_tabela_servico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

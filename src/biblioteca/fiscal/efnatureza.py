# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efnatureza (Naturezas de operação (CFOP)) - módulo fiscal."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efnatureza"
MODULO = "fiscal"
ENTIDADES = ['natureza_operacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_simples_nacional_anexo (Simples Nacional - Anexos) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_simples_nacional_anexo"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_simples_nacional_anexo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

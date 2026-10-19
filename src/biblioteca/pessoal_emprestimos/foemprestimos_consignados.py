# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foemprestimos_consignados (Empréstimos consignados.) - módulo pessoal_emprestimos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foemprestimos_consignados"
MODULO = "pessoal_emprestimos"
ENTIDADES = ['foemprestimos_consignados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

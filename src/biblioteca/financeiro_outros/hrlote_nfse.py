# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrlote_nfse (Lotes para notas fiscais de servico eletronica emitidas) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrlote_nfse"
MODULO = "financeiro_outros"
ENTIDADES = ['hrlote_nfse']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

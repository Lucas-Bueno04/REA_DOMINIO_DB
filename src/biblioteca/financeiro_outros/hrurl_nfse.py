# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrurl_nfse (Armazena as RULs usadas na nota fiscal de servico eletronica) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrurl_nfse"
MODULO = "financeiro_outros"
ENTIDADES = ['hrurl_nfse']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

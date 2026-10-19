# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrcodigo_cancelamento_nfse (Código de cancelamento NFS-e Tecnospeed) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrcodigo_cancelamento_nfse"
MODULO = "financeiro_outros"
ENTIDADES = ['hrcodigo_cancelamento_nfse']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

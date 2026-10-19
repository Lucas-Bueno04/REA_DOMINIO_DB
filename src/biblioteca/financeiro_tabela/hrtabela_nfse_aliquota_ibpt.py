# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrtabela_nfse_aliquota_ibpt (Tabela Alíquota de impostos conforme IBPT) - módulo financeiro_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrtabela_nfse_aliquota_ibpt"
MODULO = "financeiro_tabela"
ENTIDADES = ['hrtabela_nfse_aliquota_ibpt']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

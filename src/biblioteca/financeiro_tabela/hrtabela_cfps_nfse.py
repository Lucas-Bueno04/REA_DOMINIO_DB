# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrtabela_cfps_nfse (Tabela Codigo Fiscal de Prestacoes de Servicos - NFSE) - módulo financeiro_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrtabela_cfps_nfse"
MODULO = "financeiro_tabela"
ENTIDADES = ['hrtabela_cfps_nfse']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

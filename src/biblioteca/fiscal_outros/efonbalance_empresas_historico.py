# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efonbalance_empresas_historico (log de alteraÃ§Ãµes da tabela EFONBALANCE_EMPRESAS) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efonbalance_empresas_historico"
MODULO = "fiscal_outros"
ENTIDADES = ['efonbalance_empresas_historico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

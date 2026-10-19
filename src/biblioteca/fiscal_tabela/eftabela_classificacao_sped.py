# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_classificacao_sped (Tabela de classificacao de servicos do SPED fiscal) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_classificacao_sped"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_classificacao_sped']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela cttabela_sped_ecf_natureza_operacao (SPED ECF - Tabela de natureza da operação) - módulo contabil_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "cttabela_sped_ecf_natureza_operacao"
MODULO = "contabil_tabela"
ENTIDADES = ['cttabela_sped_ecf_natureza_operacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela cttabela_sped_ecf_tipo_moeda (SPED ECF - Tabela Tipos de Moedas) - módulo contabil_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "cttabela_sped_ecf_tipo_moeda"
MODULO = "contabil_tabela"
ENTIDADES = ['cttabela_sped_ecf_tipo_moeda']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

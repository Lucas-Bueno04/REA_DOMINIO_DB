# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela cttabela_sped_ecf_od_registro (Layout dos registros do SPED ECF (tabela de colunas)) - módulo sped_ecf."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "cttabela_sped_ecf_od_registro"
MODULO = "sped_ecf"
ENTIDADES = ['layout_registro_ecf']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

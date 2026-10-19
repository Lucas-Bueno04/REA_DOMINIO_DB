# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctsped_ecf_od_w100 (SPED ECF - Outros Dados - Registro W100) - módulo contabil_sped."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctsped_ecf_od_w100"
MODULO = "contabil_sped"
ENTIDADES = ['ctsped_ecf_od_w100']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

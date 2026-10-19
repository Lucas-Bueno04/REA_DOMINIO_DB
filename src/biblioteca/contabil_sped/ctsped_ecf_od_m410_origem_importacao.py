# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctsped_ecf_od_m410_origem_importacao (Tabela de origem da importação registros M410) - módulo contabil_sped."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctsped_ecf_od_m410_origem_importacao"
MODULO = "contabil_sped"
ENTIDADES = ['ctsped_ecf_od_m410_origem_importacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

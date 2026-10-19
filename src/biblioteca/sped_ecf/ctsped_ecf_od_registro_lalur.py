# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctsped_ecf_od_registro_lalur (ECF - Registros do Lalur (Parte A/B)) - módulo sped_ecf."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctsped_ecf_od_registro_lalur"
MODULO = "sped_ecf"
ENTIDADES = ['valor_lalur_ecf']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

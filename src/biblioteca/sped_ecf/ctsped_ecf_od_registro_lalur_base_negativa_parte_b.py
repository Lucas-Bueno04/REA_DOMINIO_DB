# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctsped_ecf_od_registro_lalur_base_negativa_parte_b (ECF - Base negativa da Parte B do Lalur) - módulo sped_ecf."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctsped_ecf_od_registro_lalur_base_negativa_parte_b"
MODULO = "sped_ecf"
ENTIDADES = ['base_negativa_parte_b_ecf']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

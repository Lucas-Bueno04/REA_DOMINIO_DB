# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecontrole_imposto_retido (Controle do recolhimento do imposto retido - IRRF) - módulo geral_controle."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecontrole_imposto_retido"
MODULO = "geral_controle"
ENTIDADES = ['gecontrole_imposto_retido']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

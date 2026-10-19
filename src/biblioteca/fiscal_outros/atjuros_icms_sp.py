# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela atjuros_icms_sp (Tabela de juros de ICMS para SP) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "atjuros_icms_sp"
MODULO = "fiscal_outros"
ENTIDADES = ['atjuros_icms_sp']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

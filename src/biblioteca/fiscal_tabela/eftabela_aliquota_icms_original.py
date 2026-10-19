# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_aliquota_icms_original (Tabela de Alíquota Interestadual de ICMS - Original) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_aliquota_icms_original"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_aliquota_icms_original']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

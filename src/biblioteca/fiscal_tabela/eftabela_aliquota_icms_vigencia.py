# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_aliquota_icms_vigencia (Tabela de Alíquota Interestadual de ICMS - Vigência) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_aliquota_icms_vigencia"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_aliquota_icms_vigencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

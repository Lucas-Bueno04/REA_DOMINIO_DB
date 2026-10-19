# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_aliquota_efetiva_icms_st_at_vigencia (Tabela de Alíquota Efetiva de ICMS STAT - Vigência) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_aliquota_efetiva_icms_st_at_vigencia"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_aliquota_efetiva_icms_st_at_vigencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

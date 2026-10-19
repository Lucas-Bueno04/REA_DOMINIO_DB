# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_icms_st_carga_media (Tabela ICMS ST Estimativa Simplificado - Carga Média) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_icms_st_carga_media"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_icms_st_carga_media']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

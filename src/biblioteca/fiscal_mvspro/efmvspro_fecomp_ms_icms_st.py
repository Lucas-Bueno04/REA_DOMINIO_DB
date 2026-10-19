# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvspro_fecomp_ms_icms_st (Notas Fiscais de Saída - Produtos - FECOMP ST MS) - módulo fiscal_mvspro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvspro_fecomp_ms_icms_st"
MODULO = "fiscal_mvspro"
ENTIDADES = ['efmvspro_fecomp_ms_icms_st']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

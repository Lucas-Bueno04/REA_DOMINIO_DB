# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvspro_fecomp_ms_icms_proprio (Notas Fiscais de Saída - Produtos - FECOMP MS) - módulo fiscal_mvspro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvspro_fecomp_ms_icms_proprio"
MODULO = "fiscal_mvspro"
ENTIDADES = ['efmvspro_fecomp_ms_icms_proprio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

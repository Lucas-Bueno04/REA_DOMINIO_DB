# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvepro_icms_stat (Notas Fiscais de Entrada - Produtos - ICMS STAT) - módulo fiscal_mvepro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvepro_icms_stat"
MODULO = "fiscal_mvepro"
ENTIDADES = ['efmvepro_icms_stat']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

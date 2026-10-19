# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvspro_ibs_iva (Valorer IBS Estoque - Saidas) - módulo fiscal_mvspro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvspro_ibs_iva"
MODULO = "fiscal_mvspro"
ENTIDADES = ['efmvspro_ibs_iva']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

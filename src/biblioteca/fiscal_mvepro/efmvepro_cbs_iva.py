# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvepro_cbs_iva (Valorer CBS Estoque - Entradas) - módulo fiscal_mvepro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvepro_cbs_iva"
MODULO = "fiscal_mvepro"
ENTIDADES = ['efmvepro_cbs_iva']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvepro_difal_nc (Notas Fiscais de Entrada - Produtos - DIFAL NC) - módulo fiscal_mvepro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvepro_difal_nc"
MODULO = "fiscal_mvepro"
ENTIDADES = ['efmvepro_difal_nc']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

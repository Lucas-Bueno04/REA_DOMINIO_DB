# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvspro_difal_nc (Notas Fiscais de Saida - Produtos - DIFAL NC) - módulo fiscal_mvspro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvspro_difal_nc"
MODULO = "fiscal_mvspro"
ENTIDADES = ['efmvspro_difal_nc']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

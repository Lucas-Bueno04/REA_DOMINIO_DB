# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvvpro_cbs_iva (Notas Fiscais de Serviços - Produtos) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvvpro_cbs_iva"
MODULO = "fiscal_outros"
ENTIDADES = ['efmvvpro_cbs_iva']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

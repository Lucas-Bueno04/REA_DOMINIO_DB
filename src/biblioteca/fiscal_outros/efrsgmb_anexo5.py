# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efrsgmb_anexo5 (GMB - Tabela de Codigos Fiscais) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efrsgmb_anexo5"
MODULO = "fiscal_outros"
ENTIDADES = ['efrsgmb_anexo5']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

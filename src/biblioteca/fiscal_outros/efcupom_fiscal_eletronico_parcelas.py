# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcupom_fiscal_eletronico_parcelas (Cupom Fiscal Eletrônico - CF-e - Parcelas) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcupom_fiscal_eletronico_parcelas"
MODULO = "fiscal_outros"
ENTIDADES = ['efcupom_fiscal_eletronico_parcelas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcupom_fiscal_eletronico_pagamentos (Cupom Fiscal Eletrônico - CF-e - Parcelas - Pagamentos) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcupom_fiscal_eletronico_pagamentos"
MODULO = "fiscal_outros"
ENTIDADES = ['efcupom_fiscal_eletronico_pagamentos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

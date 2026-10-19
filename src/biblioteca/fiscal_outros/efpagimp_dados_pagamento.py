# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efpagimp_dados_pagamento (Pagamentos de Impostos - guia) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efpagimp_dados_pagamento"
MODULO = "fiscal_outros"
ENTIDADES = ['efpagimp_dados_pagamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

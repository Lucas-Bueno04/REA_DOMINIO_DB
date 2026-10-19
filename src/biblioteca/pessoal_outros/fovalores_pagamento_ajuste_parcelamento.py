# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fovalores_pagamento_ajuste_parcelamento (Valores dos pagamentos das diferenças do ajuste conforme parcelamento) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fovalores_pagamento_ajuste_parcelamento"
MODULO = "pessoal_outros"
ENTIDADES = ['fovalores_pagamento_ajuste_parcelamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

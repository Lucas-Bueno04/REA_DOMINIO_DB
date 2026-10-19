# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcontas_bc_instituicao_pagamento (Plano de contas Banco Central - Administradoras de Consórcio) - módulo contabil_contas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcontas_bc_instituicao_pagamento"
MODULO = "contabil_contas"
ENTIDADES = ['ctcontas_bc_instituicao_pagamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

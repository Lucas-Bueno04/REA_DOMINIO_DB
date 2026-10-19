# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fopagto_dados_pagamento (Pagamentos de Impostos - Publicação) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fopagto_dados_pagamento"
MODULO = "pessoal_outros"
ENTIDADES = ['fopagto_dados_pagamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

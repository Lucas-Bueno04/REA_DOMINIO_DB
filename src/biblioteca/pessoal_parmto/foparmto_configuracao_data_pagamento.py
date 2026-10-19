# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foparmto_configuracao_data_pagamento (Configurações para as datas de pagamento dos cálculos da folha.) - módulo pessoal_parmto."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foparmto_configuracao_data_pagamento"
MODULO = "pessoal_parmto"
ENTIDADES = ['foparmto_configuracao_data_pagamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

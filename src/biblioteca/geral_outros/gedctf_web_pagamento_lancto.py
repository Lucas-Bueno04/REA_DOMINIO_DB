# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gedctf_web_pagamento_lancto (DCTF Web - Pagamentos X Lançamentos contábeis) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gedctf_web_pagamento_lancto"
MODULO = "geral_outros"
ENTIDADES = ['gedctf_web_pagamento_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

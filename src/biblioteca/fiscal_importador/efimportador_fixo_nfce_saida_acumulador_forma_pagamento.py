# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_nfce_saida_acumulador_forma_pagamento (Configuração do leiaute NFC-e XML do Importador Fixo - Saída - Acumulador - Forma de pagamento) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_nfce_saida_acumulador_forma_pagamento"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_nfce_saida_acumulador_forma_pagamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

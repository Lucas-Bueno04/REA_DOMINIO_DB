# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_mg_sub_apuracao_incentivo_ret (Saldo dos Impostos - Sub Apuração MG - Incentivo RET) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_mg_sub_apuracao_incentivo_ret"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_mg_sub_apuracao_incentivo_ret']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

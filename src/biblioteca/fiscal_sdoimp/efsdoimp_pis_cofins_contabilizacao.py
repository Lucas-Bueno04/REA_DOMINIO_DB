# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_pis_cofins_contabilizacao (Saldo do Impostos - ContabilizaÃ§Ã£o do PIS/COFINS) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_pis_cofins_contabilizacao"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_pis_cofins_contabilizacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_pis_cofins_reducao_linear_por_nota (Saldo do Impostos - PIS/COFINS Reducao Linear por Nota) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_pis_cofins_reducao_linear_por_nota"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_pis_cofins_reducao_linear_por_nota']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

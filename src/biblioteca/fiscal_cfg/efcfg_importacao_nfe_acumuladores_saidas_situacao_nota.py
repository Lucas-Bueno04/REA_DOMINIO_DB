# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcfg_importacao_nfe_acumuladores_saidas_situacao_nota (Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores - Situação da Nota) - módulo fiscal_cfg."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcfg_importacao_nfe_acumuladores_saidas_situacao_nota"
MODULO = "fiscal_cfg"
ENTIDADES = ['efcfg_importacao_nfe_acumuladores_saidas_situacao_nota']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcfg_importacao_nfe_acumuladores_servicos_item_servico (Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores - Item serviço) - módulo fiscal_cfg."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcfg_importacao_nfe_acumuladores_servicos_item_servico"
MODULO = "fiscal_cfg"
ENTIDADES = ['efcfg_importacao_nfe_acumuladores_servicos_item_servico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

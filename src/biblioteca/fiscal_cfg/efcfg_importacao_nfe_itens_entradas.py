# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcfg_importacao_nfe_itens_entradas (Importação NFS-e Paulistana - Entrada - Relacionamento de itens) - módulo fiscal_cfg."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcfg_importacao_nfe_itens_entradas"
MODULO = "fiscal_cfg"
ENTIDADES = ['efcfg_importacao_nfe_itens_entradas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

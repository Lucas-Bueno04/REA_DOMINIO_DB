# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcfg_importacao_nfe_acumuladores_servicos_clientes_selecionados (Configuracao de importacao de NFS-e Paulistana - Acumuladores - Definição de clientes selecionados) - módulo fiscal_cfg."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcfg_importacao_nfe_acumuladores_servicos_clientes_selecionados"
MODULO = "fiscal_cfg"
ENTIDADES = ['efcfg_importacao_nfe_acumuladores_servicos_clientes_selecion']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

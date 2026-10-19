# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efconfiguracao_produto_por_ncm_vigencia_itens (Configuração de Impostos para Produtos - Registros) - módulo fiscal_configuracao."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efconfiguracao_produto_por_ncm_vigencia_itens"
MODULO = "fiscal_configuracao"
ENTIDADES = ['efconfiguracao_produto_por_ncm_vigencia_itens']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

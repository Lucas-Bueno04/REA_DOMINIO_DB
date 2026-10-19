# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efconfiguracao_produto_por_ncm (Configurar Dados de Impostos por NCM) - módulo fiscal_configuracao."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efconfiguracao_produto_por_ncm"
MODULO = "fiscal_configuracao"
ENTIDADES = ['efconfiguracao_produto_por_ncm']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_nfe_entrada_cfop_excecao_por_fornecedor_cfop_entrada (Configuração do leiaute NF-e XML do Importador Fixo - Entrada - CFOP - Exceção por fornecedor, CFOP de entrada) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_nfe_entrada_cfop_excecao_por_fornecedor_cfop_entrada"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_nfe_entrada_cfop_excecao_por_fornecedor_cf_x']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

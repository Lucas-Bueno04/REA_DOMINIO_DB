# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_site_cte_entrada_cfop (Configuração da importação do CT-e pelo site da Receita Federal - Entrada - CFOP) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_site_cte_entrada_cfop"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_site_cte_entrada_cfop']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

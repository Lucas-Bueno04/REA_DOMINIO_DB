# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrlucro_antes_csll_irpj (Lucro antes da CSLL e do IRPJ (apurado na contabilidade)) - módulo lalur."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrlucro_antes_csll_irpj"
MODULO = "lalur"
ENTIDADES = ['lucro_antes_irpj_csll']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

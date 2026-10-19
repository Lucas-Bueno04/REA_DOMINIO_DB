# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrirpj_real_adicao_item (Lançamentos de Adições do Imposto de Renda - Adições) - módulo contabil_irpj."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrirpj_real_adicao_item"
MODULO = "contabil_irpj"
ENTIDADES = ['lrirpj_real_adicao_item']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

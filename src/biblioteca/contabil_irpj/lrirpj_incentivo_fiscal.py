# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrirpj_incentivo_fiscal (Lançamentos de Incentivos Fiscais) - módulo contabil_irpj."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrirpj_incentivo_fiscal"
MODULO = "contabil_irpj"
ENTIDADES = ['lrirpj_incentivo_fiscal']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

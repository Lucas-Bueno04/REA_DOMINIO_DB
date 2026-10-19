# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrirpj_estimado_deducao (Deduções do Imposto de Renda (Estimado)) - módulo contabil_irpj."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrirpj_estimado_deducao"
MODULO = "contabil_irpj"
ENTIDADES = ['lrirpj_estimado_deducao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

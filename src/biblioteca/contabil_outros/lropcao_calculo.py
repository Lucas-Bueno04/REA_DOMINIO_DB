# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lropcao_calculo (Opções de Cálculo) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lropcao_calculo"
MODULO = "contabil_outros"
ENTIDADES = ['lropcao_calculo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

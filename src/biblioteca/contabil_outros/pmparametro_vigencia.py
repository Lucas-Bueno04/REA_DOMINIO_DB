# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmparametro_vigencia (Parâmetros - Patrimônio - Vigência) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmparametro_vigencia"
MODULO = "contabil_outros"
ENTIDADES = ['pmparametro_vigencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

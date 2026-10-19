# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrparametro_vigencia (Parametro Honorarios - Vigencia) - módulo financeiro_parametro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrparametro_vigencia"
MODULO = "financeiro_parametro"
ENTIDADES = ['hrparametro_vigencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

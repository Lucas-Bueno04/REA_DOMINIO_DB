# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_dere_concursos (DeRE - Concursos de prognósticos) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_dere_concursos"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_dere_concursos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

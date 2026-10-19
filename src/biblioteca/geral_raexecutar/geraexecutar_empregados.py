# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geraexecutar_empregados (Rotinas automáticas - Empregados executar) - módulo geral_raexecutar."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geraexecutar_empregados"
MODULO = "geral_raexecutar"
ENTIDADES = ['geraexecutar_empregados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

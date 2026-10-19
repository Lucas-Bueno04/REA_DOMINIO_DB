# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fovariavel_planosaude (Lançamentos - Processos - Plano de saúde) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fovariavel_planosaude"
MODULO = "pessoal_outros"
ENTIDADES = ['fovariavel_planosaude']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

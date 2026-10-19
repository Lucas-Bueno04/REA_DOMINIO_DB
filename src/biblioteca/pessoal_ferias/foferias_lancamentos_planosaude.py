# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foferias_lancamentos_planosaude (Lançamentos de férias - Processos - Plano de saúde) - módulo pessoal_ferias."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foferias_lancamentos_planosaude"
MODULO = "pessoal_ferias"
ENTIDADES = ['foferias_lancamentos_planosaude']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

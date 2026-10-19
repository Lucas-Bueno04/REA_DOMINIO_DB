# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foferias_lancamentos_pensao_alimenticia (Valores de pensão alimentícia nas férias por dependente.) - módulo pessoal_ferias."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foferias_lancamentos_pensao_alimenticia"
MODULO = "pessoal_ferias"
ENTIDADES = ['foferias_lancamentos_pensao_alimenticia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela folancamentos_eventos_pensao_alimenticia (Valores de pensão alimentícia por dependente.) - módulo pessoal_lancamentos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "folancamentos_eventos_pensao_alimenticia"
MODULO = "pessoal_lancamentos"
ENTIDADES = ['folancamentos_eventos_pensao_alimenticia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

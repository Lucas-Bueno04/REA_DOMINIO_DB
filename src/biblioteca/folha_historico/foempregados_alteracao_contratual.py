# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foempregados_alteracao_contratual (Alterações contratuais do empregado) - módulo folha_historico."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foempregados_alteracao_contratual"
MODULO = "folha_historico"
ENTIDADES = ['alteracao_contratual']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

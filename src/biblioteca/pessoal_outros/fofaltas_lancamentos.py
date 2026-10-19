# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fofaltas_lancamentos (RELACIONAMENTO ENTRE FALTAS E LANCAMENTOS) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fofaltas_lancamentos"
MODULO = "pessoal_outros"
ENTIDADES = ['fofaltas_lancamentos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

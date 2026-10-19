# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctnotas_explicativas_relacionamento_conta (Notas explicativas - Relacionamento entre contas - Contas) - módulo contabil_notas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctnotas_explicativas_relacionamento_conta"
MODULO = "contabil_notas"
ENTIDADES = ['ctnotas_explicativas_relacionamento_conta']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

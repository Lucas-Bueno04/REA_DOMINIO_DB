# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela getabela_grupo_tributo (Grupo de Tributo) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "getabela_grupo_tributo"
MODULO = "geral_outros"
ENTIDADES = ['getabela_grupo_tributo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

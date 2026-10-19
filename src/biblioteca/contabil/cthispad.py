# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela cthispad (Históricos padrão) - módulo contabil."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "cthispad"
MODULO = "contabil"
ENTIDADES = ['historico_padrao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela atcontrole_tabela_selic (Controle de atualização da tabela SELIC) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "atcontrole_tabela_selic"
MODULO = "fiscal_outros"
ENTIDADES = ['atcontrole_tabela_selic']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

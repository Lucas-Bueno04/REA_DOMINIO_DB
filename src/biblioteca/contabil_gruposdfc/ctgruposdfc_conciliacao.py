# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctgruposdfc_conciliacao (Estrutura DFC - Conciliacao) - módulo contabil_gruposdfc."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctgruposdfc_conciliacao"
MODULO = "contabil_gruposdfc"
ENTIDADES = ['ctgruposdfc_conciliacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

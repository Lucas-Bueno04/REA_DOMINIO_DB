# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecontrole_execucao_threads (Controle de execução de threads ao abrir o sistema) - módulo geral_controle."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecontrole_execucao_threads"
MODULO = "geral_controle"
ENTIDADES = ['gecontrole_execucao_threads']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

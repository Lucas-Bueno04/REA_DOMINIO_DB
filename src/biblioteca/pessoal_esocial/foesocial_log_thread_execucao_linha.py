# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_log_thread_execucao_linha (Tabela de log das threads relacionadas com o eSocial) - módulo pessoal_esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_log_thread_execucao_linha"
MODULO = "pessoal_esocial"
ENTIDADES = ['foesocial_log_thread_execucao_linha']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

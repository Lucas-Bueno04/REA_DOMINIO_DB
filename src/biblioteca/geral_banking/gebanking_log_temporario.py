# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gebanking_log_temporario (Tabela de logs para monitoramento temporário de processos) - módulo geral_banking."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gebanking_log_temporario"
MODULO = "geral_banking"
ENTIDADES = ['gebanking_log_temporario']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

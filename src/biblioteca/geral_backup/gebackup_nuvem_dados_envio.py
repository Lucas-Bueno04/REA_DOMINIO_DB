# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gebackup_nuvem_dados_envio (Tabela com os dados à serem enviados para o servidor.) - módulo geral_backup."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gebackup_nuvem_dados_envio"
MODULO = "geral_backup"
ENTIDADES = ['gebackup_nuvem_dados_envio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

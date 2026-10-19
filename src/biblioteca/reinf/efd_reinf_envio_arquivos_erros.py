# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efd_reinf_envio_arquivos_erros (Erros dos envios da EFD-Reinf) - módulo reinf."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efd_reinf_envio_arquivos_erros"
MODULO = "reinf"
ENTIDADES = ['erro_envio_reinf']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

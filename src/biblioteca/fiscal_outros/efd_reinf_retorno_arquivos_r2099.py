# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efd_reinf_retorno_arquivos_r2099 (EFD-Reinf - Retorno do Web Service - R-2099) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efd_reinf_retorno_arquivos_r2099"
MODULO = "fiscal_outros"
ENTIDADES = ['efd_reinf_retorno_arquivos_r2099']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

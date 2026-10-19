# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efd_reinf_retorno_arquivos_r2099_r2050 (EFD-Reinf - Retorno do Web Service - R-2099 - R-2050) - módulo fiscal_d."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efd_reinf_retorno_arquivos_r2099_r2050"
MODULO = "fiscal_d"
ENTIDADES = ['efd_reinf_retorno_arquivos_r2099_r2050']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

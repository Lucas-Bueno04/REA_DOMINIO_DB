# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efd_reinf_retorno_arquivos_r4099_periodo (EFD-Reinf - Retorno do Web Service - R-4099 - Periodo) - módulo fiscal_d."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efd_reinf_retorno_arquivos_r4099_periodo"
MODULO = "fiscal_d"
ENTIDADES = ['efd_reinf_retorno_arquivos_r4099_periodo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

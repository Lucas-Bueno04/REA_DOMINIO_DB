# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_subtri_por_uf (Apuração do ICMS-ST por UF) - módulo icms."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_subtri_por_uf"
MODULO = "icms"
ENTIDADES = ['apuracao_icms_st_uf']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

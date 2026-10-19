# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_importacao_sst_log (Log de importações da FOESOCIAL_IMPORTACAO_SST) - módulo pessoal_esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_importacao_sst_log"
MODULO = "pessoal_esocial"
ENTIDADES = ['foesocial_importacao_sst_log']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

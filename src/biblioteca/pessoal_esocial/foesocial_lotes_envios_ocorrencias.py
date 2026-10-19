# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_lotes_envios_ocorrencias (Ocorrências do lote de envio) - módulo pessoal_esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_lotes_envios_ocorrencias"
MODULO = "pessoal_esocial"
ENTIDADES = ['foesocial_lotes_envios_ocorrencias']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

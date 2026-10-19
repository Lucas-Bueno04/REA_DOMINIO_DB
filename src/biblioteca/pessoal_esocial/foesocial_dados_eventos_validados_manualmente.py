# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_dados_eventos_validados_manualmente (Tabela com eventos que foram validados manualmente pelo sistema.) - módulo pessoal_esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_dados_eventos_validados_manualmente"
MODULO = "pessoal_esocial"
ENTIDADES = ['foesocial_dados_eventos_validados_manualmente']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

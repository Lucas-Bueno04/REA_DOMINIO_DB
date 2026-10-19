# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_fila_eventos_gerar (Fila de eventos para gerar o XML do eSocial.) - módulo pessoal_esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_fila_eventos_gerar"
MODULO = "pessoal_esocial"
ENTIDADES = ['foesocial_fila_eventos_gerar']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

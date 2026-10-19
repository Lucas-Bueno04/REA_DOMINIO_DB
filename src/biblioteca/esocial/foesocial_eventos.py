# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_eventos (Catálogo dos eventos do eSocial) - módulo esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_eventos"
MODULO = "esocial"
ENTIDADES = ['catalogo_evento_esocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

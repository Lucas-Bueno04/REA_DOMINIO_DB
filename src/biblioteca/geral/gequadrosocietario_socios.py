# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gequadrosocietario_socios (Participantes do quadro societário) - módulo geral."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gequadrosocietario_socios"
MODULO = "geral"
ENTIDADES = ['participante_societario']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fodirf_descricoes_outros_eventos (DIRF - Descrições outros rendimentos isentos e não tributáveis - Eventos) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fodirf_descricoes_outros_eventos"
MODULO = "pessoal_outros"
ENTIDADES = ['fodirf_descricoes_outros_eventos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

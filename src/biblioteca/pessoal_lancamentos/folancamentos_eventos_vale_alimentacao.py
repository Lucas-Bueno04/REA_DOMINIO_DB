# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela folancamentos_eventos_vale_alimentacao (Lançamentos de vale alimentação.) - módulo pessoal_lancamentos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "folancamentos_eventos_vale_alimentacao"
MODULO = "pessoal_lancamentos"
ENTIDADES = ['folancamentos_eventos_vale_alimentacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

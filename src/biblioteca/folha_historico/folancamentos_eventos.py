# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela folancamentos_eventos (Lançamentos de eventos da folha (variáveis e fixos)) - módulo folha_historico."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "folancamentos_eventos"
MODULO = "folha_historico"
ENTIDADES = ['lancamento_evento_folha']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

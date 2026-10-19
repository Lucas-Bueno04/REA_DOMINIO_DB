# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pcmovimento_atividade_responsavel (Movimentos atividades - Responsáveis) - módulo processos_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pcmovimento_atividade_responsavel"
MODULO = "processos_outros"
ENTIDADES = ['pcmovimento_atividade_responsavel']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

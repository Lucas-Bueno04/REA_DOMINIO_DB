# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimentoacoes_onvio (Ações à serem enviadas para o Onvio.) - módulo geral_atendimentoacoes."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimentoacoes_onvio"
MODULO = "geral_atendimentoacoes"
ENTIDADES = ['geatendimentoacoes_onvio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

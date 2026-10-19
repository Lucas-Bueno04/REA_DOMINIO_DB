# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimentoacoes_onvio_avisos (Avisos gerados pelas ações enviadas ao Onvio.) - módulo geral_atendimentoacoes."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimentoacoes_onvio_avisos"
MODULO = "geral_atendimentoacoes"
ENTIDADES = ['geatendimentoacoes_onvio_avisos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

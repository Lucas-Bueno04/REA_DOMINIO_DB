# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_ingestao_eventos (Controle de eventos eSocial enviados para a API de ingestão (imediato e noturno)) - módulo pessoal_esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_ingestao_eventos"
MODULO = "pessoal_esocial"
ENTIDADES = ['foesocial_ingestao_eventos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

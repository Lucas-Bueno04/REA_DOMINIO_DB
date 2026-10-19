# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_controle_periodos_dados_eventos (Lista de envios de abertura/fechamento do período para o eSocial.) - módulo pessoal_esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_controle_periodos_dados_eventos"
MODULO = "pessoal_esocial"
ENTIDADES = ['foesocial_controle_periodos_dados_eventos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

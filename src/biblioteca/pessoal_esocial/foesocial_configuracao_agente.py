# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_configuracao_agente (Configurações do eSocial no Agente de Comunicação.) - módulo pessoal_esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_configuracao_agente"
MODULO = "pessoal_esocial"
ENTIDADES = ['foesocial_configuracao_agente']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

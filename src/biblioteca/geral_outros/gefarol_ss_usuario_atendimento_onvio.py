# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gefarol_ss_usuario_atendimento_onvio (Usuários do Onvio que possuem solicitações pendentes) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gefarol_ss_usuario_atendimento_onvio"
MODULO = "geral_outros"
ENTIDADES = ['gefarol_ss_usuario_atendimento_onvio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

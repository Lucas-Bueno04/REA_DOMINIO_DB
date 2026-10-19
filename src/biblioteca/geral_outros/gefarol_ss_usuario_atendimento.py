# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gefarol_ss_usuario_atendimento (Situação dos atendimentos por usuário) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gefarol_ss_usuario_atendimento"
MODULO = "geral_outros"
ENTIDADES = ['gefarol_ss_usuario_atendimento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

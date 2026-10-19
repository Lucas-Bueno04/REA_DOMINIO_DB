# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foatendimento_sindicato_empresa_onvio (Tabela referente a view BETHADBA.SINDICATO_EMPRESA_ATENDIMENTO do DA antigo.) - módulo pessoal_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foatendimento_sindicato_empresa_onvio"
MODULO = "pessoal_atendimento"
ENTIDADES = ['foatendimento_sindicato_empresa_onvio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

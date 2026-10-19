# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foatendimento_servicos_empresa_onvio (Tabela para controle das GUIDs de envio pro ONVIO, mantendo comportamento do DA antigo que era feito select envolvendo multiplas tabelas.) - módulo pessoal_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foatendimento_servicos_empresa_onvio"
MODULO = "pessoal_atendimento"
ENTIDADES = ['foatendimento_servicos_empresa_onvio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

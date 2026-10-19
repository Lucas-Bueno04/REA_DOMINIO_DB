# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_onvio_empresas_ignoradas (Erros de empresas enviadas ao Onvio ignorados.) - módulo geral_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_onvio_empresas_ignoradas"
MODULO = "geral_atendimento"
ENTIDADES = ['geatendimento_onvio_empresas_ignoradas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

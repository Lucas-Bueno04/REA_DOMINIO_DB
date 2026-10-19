# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecontador_envios_esocial (Liga contadores aos eventos e-Social gerados - Tabela de relacionamento entre contador e eventos e-Social através de CODI_EMP_DADOS_EVENTOS e I_DADOS_EVENTOS) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecontador_envios_esocial"
MODULO = "geral_outros"
ENTIDADES = ['gecontador_envios_esocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

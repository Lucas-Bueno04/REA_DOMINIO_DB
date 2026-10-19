# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fobasesserv_envios_esocial (Envios de bases de cálculo para o esocial) - módulo pessoal_basesserv."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fobasesserv_envios_esocial"
MODULO = "pessoal_basesserv"
ENTIDADES = ['fobasesserv_envios_esocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

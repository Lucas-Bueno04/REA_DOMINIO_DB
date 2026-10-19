# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foavisosconf_fechamento_periodo (Configurações do aviso de competências sem fechamento no eSocial) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foavisosconf_fechamento_periodo"
MODULO = "pessoal_outros"
ENTIDADES = ['foavisosconf_fechamento_periodo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

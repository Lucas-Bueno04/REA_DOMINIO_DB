# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foavisos_vencimentos_parametros (Parâmetros dos avisos de vencimentos) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foavisos_vencimentos_parametros"
MODULO = "pessoal_outros"
ENTIDADES = ['foavisos_vencimentos_parametros']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

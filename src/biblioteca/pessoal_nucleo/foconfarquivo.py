# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foconfarquivo (Configuracao de arquivos) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foconfarquivo"
MODULO = "pessoal_nucleo"
ENTIDADES = ['foconfarquivo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foconfarquivocols (Colunas da Configuracao de Arquivos) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foconfarquivocols"
MODULO = "pessoal_nucleo"
ENTIDADES = ['foconfarquivocols']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

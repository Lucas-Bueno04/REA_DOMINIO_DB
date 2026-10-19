# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foexparquivo (Configuracao Arquivo Credito em Conta) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foexparquivo"
MODULO = "pessoal_nucleo"
ENTIDADES = ['foexparquivo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

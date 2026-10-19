# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foguiainssemissao (Controle de emissao da guia) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foguiainssemissao"
MODULO = "pessoal_nucleo"
ENTIDADES = ['foguiainssemissao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

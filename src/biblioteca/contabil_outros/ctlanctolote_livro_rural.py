# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctlanctolote_livro_rural (Informação de o lote deve ser considerado no livro rural) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctlanctolote_livro_rural"
MODULO = "contabil_outros"
ENTIDADES = ['ctlanctolote_livro_rural']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

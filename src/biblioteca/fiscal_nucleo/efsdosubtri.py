# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdosubtri (Saldo da Substituicao Tributaria por Estado) - módulo fiscal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdosubtri"
MODULO = "fiscal_nucleo"
ENTIDADES = ['efsdosubtri']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

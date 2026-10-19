# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmunici (Municipios - Cadastro) - módulo fiscal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmunici"
MODULO = "fiscal_nucleo"
ENTIDADES = ['efmunici']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

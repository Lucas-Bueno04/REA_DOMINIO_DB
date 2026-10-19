# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fobasesservirrf (Bases de Calculo - Base de IRRF) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fobasesservirrf"
MODULO = "pessoal_nucleo"
ENTIDADES = ['fobasesservirrf']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foformulas (Eventos - Cadastro - Formulas) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foformulas"
MODULO = "pessoal_nucleo"
ENTIDADES = ['foformulas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

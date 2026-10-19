# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fohorarios_intervalos (Cadastro de intervalo dos horários) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fohorarios_intervalos"
MODULO = "pessoal_outros"
ENTIDADES = ['fohorarios_intervalos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

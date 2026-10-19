# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsimples_nacional_receita_bruta_anterior (Receita bruta de períodos anteriores (Simples Nacional)) - módulo simples."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsimples_nacional_receita_bruta_anterior"
MODULO = "simples"
ENTIDADES = ['receita_bruta_anterior_simples']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

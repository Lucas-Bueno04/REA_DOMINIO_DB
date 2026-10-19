# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela folinhas_valores_passagem (Valores da passagem por competência.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "folinhas_valores_passagem"
MODULO = "pessoal_outros"
ENTIDADES = ['folinhas_valores_passagem']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

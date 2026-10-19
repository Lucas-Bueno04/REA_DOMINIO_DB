# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gepastas_moduloweb (Pastas de publicação do Onvio) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gepastas_moduloweb"
MODULO = "geral_outros"
ENTIDADES = ['gepastas_moduloweb']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

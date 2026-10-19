# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geimportador_leiautes_registros_campos (Campos dos registros dos leiautes) - módulo geral_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geimportador_leiautes_registros_campos"
MODULO = "geral_importador"
ENTIDADES = ['geimportador_leiautes_registros_campos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

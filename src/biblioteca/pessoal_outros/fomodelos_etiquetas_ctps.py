# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomodelos_etiquetas_ctps (Modelos das etiquetas de atualização da CTPS.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomodelos_etiquetas_ctps"
MODULO = "pessoal_outros"
ENTIDADES = ['fomodelos_etiquetas_ctps']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

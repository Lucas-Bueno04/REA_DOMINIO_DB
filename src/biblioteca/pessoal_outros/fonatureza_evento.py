# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fonatureza_evento (Natureza dos eventos.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fonatureza_evento"
MODULO = "pessoal_outros"
ENTIDADES = ['fonatureza_evento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

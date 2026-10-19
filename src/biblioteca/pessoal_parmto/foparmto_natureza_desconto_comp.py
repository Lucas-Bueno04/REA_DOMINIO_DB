# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foparmto_natureza_desconto_comp (Tabela de naturezas das rubricas de desconto compulsório) - módulo pessoal_parmto."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foparmto_natureza_desconto_comp"
MODULO = "pessoal_parmto"
ENTIDADES = ['foparmto_natureza_desconto_comp']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

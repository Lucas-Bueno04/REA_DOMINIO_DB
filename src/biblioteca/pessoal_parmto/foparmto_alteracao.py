# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foparmto_alteracao (Tabela de alterações de parâmetros.) - módulo pessoal_parmto."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foparmto_alteracao"
MODULO = "pessoal_parmto"
ENTIDADES = ['foparmto_alteracao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

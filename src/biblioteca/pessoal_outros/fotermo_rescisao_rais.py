# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotermo_rescisao_rais (Valores para compor o campo 23 do termo de rescisão.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotermo_rescisao_rais"
MODULO = "pessoal_outros"
ENTIDADES = ['fotermo_rescisao_rais']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

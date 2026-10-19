# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_importacoes_colaboradores (Colaboradores a serem importados do site do eSocial.) - módulo pessoal_esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_importacoes_colaboradores"
MODULO = "pessoal_esocial"
ENTIDADES = ['foesocial_importacoes_colaboradores']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

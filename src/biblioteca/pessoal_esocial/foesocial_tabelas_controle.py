# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_tabelas_controle (Tabelas que possuem as colunas de controle do eSocial.) - módulo pessoal_esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_tabelas_controle"
MODULO = "pessoal_esocial"
ENTIDADES = ['foesocial_tabelas_controle']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

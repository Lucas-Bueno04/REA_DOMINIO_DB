# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geperfil_empresa (Perfis de Empresas) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geperfil_empresa"
MODULO = "geral_outros"
ENTIDADES = ['geperfil_empresa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

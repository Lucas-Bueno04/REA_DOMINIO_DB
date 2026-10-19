# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geinformacoes_modulos (INFORMAÇÕES SOBRE OS MÓDULOS) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geinformacoes_modulos"
MODULO = "geral_outros"
ENTIDADES = ['geinformacoes_modulos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

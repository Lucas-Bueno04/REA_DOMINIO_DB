# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela getabelas_exclusao_empresa (Tabelas ordenadas para realizar a exclusão da empresa) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "getabelas_exclusao_empresa"
MODULO = "geral_outros"
ENTIDADES = ['getabelas_exclusao_empresa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

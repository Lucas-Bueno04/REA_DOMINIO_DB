# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela confatualizacao (Configuracao do gerenciador de atualizacoes) - módulo outros_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "confatualizacao"
MODULO = "outros_outros"
ENTIDADES = ['confatualizacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela getipo_arquivo_auditor (Dados dos Tipos de Arquivos.) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "getipo_arquivo_auditor"
MODULO = "geral_outros"
ENTIDADES = ['getipo_arquivo_auditor']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

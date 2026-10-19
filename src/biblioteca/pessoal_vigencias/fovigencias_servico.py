# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fovigencias_servico (Vigências serviço - Cadastro) - módulo pessoal_vigencias."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fovigencias_servico"
MODULO = "pessoal_vigencias"
ENTIDADES = ['fovigencias_servico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

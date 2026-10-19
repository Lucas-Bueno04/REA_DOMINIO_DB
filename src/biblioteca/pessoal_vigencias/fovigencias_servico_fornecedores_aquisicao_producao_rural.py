# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fovigencias_servico_fornecedores_aquisicao_producao_rural (Fornecedores para importar notas fiscais de produção rural.) - módulo pessoal_vigencias."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fovigencias_servico_fornecedores_aquisicao_producao_rural"
MODULO = "pessoal_vigencias"
ENTIDADES = ['fovigencias_servico_fornecedores_aquisicao_producao_rural']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

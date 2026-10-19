# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotipos_itens_prestacao_servico (Tipos de serviço do tomador de serviço.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotipos_itens_prestacao_servico"
MODULO = "pessoal_outros"
ENTIDADES = ['fotipos_itens_prestacao_servico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

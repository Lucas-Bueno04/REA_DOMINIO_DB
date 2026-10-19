# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foinss_empresa_receita_bruta (INSS Empresa Receita Bruta) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foinss_empresa_receita_bruta"
MODULO = "pessoal_outros"
ENTIDADES = ['foinss_empresa_receita_bruta']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

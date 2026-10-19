# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmunicipio_es_dief (Cadastro de Município - Relacionamento de código estadual com código na DIEF - ES) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmunicipio_es_dief"
MODULO = "fiscal_outros"
ENTIDADES = ['efmunicipio_es_dief']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

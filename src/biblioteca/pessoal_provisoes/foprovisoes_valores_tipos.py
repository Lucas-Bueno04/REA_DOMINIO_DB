# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foprovisoes_valores_tipos (Descrição dos tipos de valores gerados no calculo da provisão.) - módulo pessoal_provisoes."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foprovisoes_valores_tipos"
MODULO = "pessoal_provisoes"
ENTIDADES = ['foprovisoes_valores_tipos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

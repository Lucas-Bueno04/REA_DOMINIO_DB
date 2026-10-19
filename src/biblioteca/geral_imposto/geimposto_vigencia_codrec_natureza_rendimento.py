# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geimposto_vigencia_codrec_natureza_rendimento (Tabela com as naturezas de rendimento dos impostos) - módulo geral_imposto."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geimposto_vigencia_codrec_natureza_rendimento"
MODULO = "geral_imposto"
ENTIDADES = ['geimposto_vigencia_codrec_natureza_rendimento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

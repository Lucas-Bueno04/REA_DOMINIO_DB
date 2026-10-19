# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela rgtipo_alteracao_contratual (Tipo de Alteracao Contratual) - módulo societario_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "rgtipo_alteracao_contratual"
MODULO = "societario_outros"
ENTIDADES = ['rgtipo_alteracao_contratual']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focontrole_recalculo (Controle de alteração nos cálculos para recálculo) - módulo pessoal_controle."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focontrole_recalculo"
MODULO = "pessoal_controle"
ENTIDADES = ['focontrole_recalculo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

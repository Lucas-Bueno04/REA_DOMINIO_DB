# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_diferencial_aliquota_ma (Tabela Diferencial de Alíquota - MA) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_diferencial_aliquota_ma"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_diferencial_aliquota_ma']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

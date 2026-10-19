# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_percentual_mistura_combustiveis_vigencia (Tabela dos Percentuais de Mistura dos Combustíveis - Vigencia) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_percentual_mistura_combustiveis_vigencia"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_percentual_mistura_combustiveis_vigencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efparametro_vigencia_impostos (Impostos ativos em cada vigência dos parâmetros fiscais) - módulo parametro_fiscal."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efparametro_vigencia_impostos"
MODULO = "parametro_fiscal"
ENTIDADES = ['parametro_fiscal_imposto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

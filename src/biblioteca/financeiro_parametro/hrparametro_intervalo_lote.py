# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrparametro_intervalo_lote (Parametro Honorarios - Intervalo de Lote) - módulo financeiro_parametro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrparametro_intervalo_lote"
MODULO = "financeiro_parametro"
ENTIDADES = ['hrparametro_intervalo_lote']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

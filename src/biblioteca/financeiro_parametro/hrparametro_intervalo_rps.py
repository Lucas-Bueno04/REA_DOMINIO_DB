# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrparametro_intervalo_rps (Parametro Honorarios - Intervalo de RPS) - módulo financeiro_parametro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrparametro_intervalo_rps"
MODULO = "financeiro_parametro"
ENTIDADES = ['hrparametro_intervalo_rps']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

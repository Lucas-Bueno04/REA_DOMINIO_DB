# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foccustos_exposicao_fatores_risco_i (Tabela de Exposição a Fatores de Riscos I referente ao cargo do empregado) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foccustos_exposicao_fatores_risco_i"
MODULO = "pessoal_outros"
ENTIDADES = ['foccustos_exposicao_fatores_risco_i']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

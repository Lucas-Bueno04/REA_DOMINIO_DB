# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focalculos_alteracao_salarial (Cálculos que pagaram alterações salariais) - módulo pessoal_calculos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focalculos_alteracao_salarial"
MODULO = "pessoal_calculos"
ENTIDADES = ['focalculos_alteracao_salarial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

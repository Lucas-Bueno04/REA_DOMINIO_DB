# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focondicoes_ambientais_trabalho_unidade_medida_fator_risco (Tabela de catálogo das unidades de medida dos fatores de risco das condições ambientais de trabalho) - módulo pessoal_condicoes."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focondicoes_ambientais_trabalho_unidade_medida_fator_risco"
MODULO = "pessoal_condicoes"
ENTIDADES = ['focondicoes_ambientais_trabalho_unidade_medida_fator_risco']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

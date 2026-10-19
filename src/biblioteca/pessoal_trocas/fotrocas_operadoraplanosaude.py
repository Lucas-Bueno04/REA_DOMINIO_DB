# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotrocas_operadoraplanosaude (** SEM USO ** Trocas de operadora de plano de saúde) - módulo pessoal_trocas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotrocas_operadoraplanosaude"
MODULO = "pessoal_trocas"
ENTIDADES = ['fotrocas_operadoraplanosaude']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

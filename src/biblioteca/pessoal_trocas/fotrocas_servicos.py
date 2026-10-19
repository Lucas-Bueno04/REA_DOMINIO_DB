# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotrocas_servicos (Trocas de servicos) - módulo pessoal_trocas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotrocas_servicos"
MODULO = "pessoal_trocas"
ENTIDADES = ['fotrocas_servicos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

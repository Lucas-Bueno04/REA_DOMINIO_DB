# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_simples_nacional_salao_parceiro (Saldo dos Impostos - Detalhamento do Simples Nacional - Salão-parceiro) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_simples_nacional_salao_parceiro"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_simples_nacional_salao_parceiro']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

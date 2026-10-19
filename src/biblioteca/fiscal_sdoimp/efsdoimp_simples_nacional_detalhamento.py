# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_simples_nacional_detalhamento (Saldo dos Impostos - Simples Nacional - Exigibilidade Suspensa) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_simples_nacional_detalhamento"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_simples_nacional_detalhamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_simples_nacional_controle_base_negativa_devolucao_secundaria (Saldo Simples Nacional Controle Base de Base Negativa Devolução Secundária 2025) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_simples_nacional_controle_base_negativa_devolucao_secundaria"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_simples_nacional_controle_base_negativa_devolucao_s']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

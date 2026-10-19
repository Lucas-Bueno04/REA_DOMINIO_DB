# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsaidas_estadual_rj (Notas Fiscais de Saídas - Dados estaduais - RJ) - módulo fiscal_saidas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsaidas_estadual_rj"
MODULO = "fiscal_saidas"
ENTIDADES = ['efsaidas_estadual_rj']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

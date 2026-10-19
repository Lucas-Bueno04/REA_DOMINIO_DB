# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsaidas_estadual_sc (Notas Fiscais de Saídas - Dados estaduais - SC) - módulo fiscal_saidas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsaidas_estadual_sc"
MODULO = "fiscal_saidas"
ENTIDADES = ['efsaidas_estadual_sc']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

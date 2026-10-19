# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsaidas_difal_nc (Notas Fiscais de Saida - DIFAL NC) - módulo fiscal_saidas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsaidas_difal_nc"
MODULO = "fiscal_saidas"
ENTIDADES = ['efsaidas_difal_nc']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

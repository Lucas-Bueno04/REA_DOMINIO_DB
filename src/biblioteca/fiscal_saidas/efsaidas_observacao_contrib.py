# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsaidas_observacao_contrib (Notas Fiscais de Saídas - Obseração de interesse do contribuinte) - módulo fiscal_saidas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsaidas_observacao_contrib"
MODULO = "fiscal_saidas"
ENTIDADES = ['efsaidas_observacao_contrib']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

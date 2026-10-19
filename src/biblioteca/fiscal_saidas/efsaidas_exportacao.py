# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsaidas_exportacao (Notas Fiscais de Saida - Exportacao do PER/DCOMP) - módulo fiscal_saidas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsaidas_exportacao"
MODULO = "fiscal_saidas"
ENTIDADES = ['efsaidas_exportacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

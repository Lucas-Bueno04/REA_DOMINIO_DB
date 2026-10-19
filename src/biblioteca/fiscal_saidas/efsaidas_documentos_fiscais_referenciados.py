# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsaidas_documentos_fiscais_referenciados (Notas Fiscais de Saída - Documentos fiscais referenciados) - módulo fiscal_saidas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsaidas_documentos_fiscais_referenciados"
MODULO = "fiscal_saidas"
ENTIDADES = ['efsaidas_documentos_fiscais_referenciados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

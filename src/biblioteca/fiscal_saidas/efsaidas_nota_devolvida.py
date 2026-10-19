# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsaidas_nota_devolvida (Notas Fiscais de Saída - Complementar - Geral - Nota Devolvida) - módulo fiscal_saidas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsaidas_nota_devolvida"
MODULO = "fiscal_saidas"
ENTIDADES = ['efsaidas_nota_devolvida']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

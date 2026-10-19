# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsaidas_inss_rb (Notas Fiscais de Saídas - INSS Receita Bruta) - módulo fiscal_saidas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsaidas_inss_rb"
MODULO = "fiscal_saidas"
ENTIDADES = ['efsaidas_inss_rb']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

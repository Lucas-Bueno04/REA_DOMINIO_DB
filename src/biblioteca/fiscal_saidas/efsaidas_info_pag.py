# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsaidas_info_pag (Notas Fiscais de Saidas - Informação Pagamento) - módulo fiscal_saidas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsaidas_info_pag"
MODULO = "fiscal_saidas"
ENTIDADES = ['efsaidas_info_pag']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

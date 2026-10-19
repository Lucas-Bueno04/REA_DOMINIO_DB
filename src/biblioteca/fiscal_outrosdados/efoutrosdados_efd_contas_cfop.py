# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoutrosdados_efd_contas_cfop (EFD Contribuições - Outros Dados - Contas - CFOP) - módulo fiscal_outrosdados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoutrosdados_efd_contas_cfop"
MODULO = "fiscal_outrosdados"
ENTIDADES = ['efoutrosdados_efd_contas_cfop']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

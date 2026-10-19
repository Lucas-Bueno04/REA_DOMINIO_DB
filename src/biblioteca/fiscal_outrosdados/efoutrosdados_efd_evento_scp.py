# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoutrosdados_efd_evento_scp (EFD Contribuições - Outros Dados - SCP) - módulo fiscal_outrosdados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoutrosdados_efd_evento_scp"
MODULO = "fiscal_outrosdados"
ENTIDADES = ['efoutrosdados_efd_evento_scp']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

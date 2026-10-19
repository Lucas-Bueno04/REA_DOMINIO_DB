# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoutrosdados_reinf_rendimentos_isentos_contas (REINF - Outros Dados - Rendimentos Isentos - Contas) - módulo fiscal_outrosdados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoutrosdados_reinf_rendimentos_isentos_contas"
MODULO = "fiscal_outrosdados"
ENTIDADES = ['efoutrosdados_reinf_rendimentos_isentos_contas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoutrosdados_efd_reinf_servicos_prestados (EFD-Reinf - Outros Dados - Serviçoes Tomados) - módulo fiscal_outrosdados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoutrosdados_efd_reinf_servicos_prestados"
MODULO = "fiscal_outrosdados"
ENTIDADES = ['efoutrosdados_efd_reinf_servicos_prestados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

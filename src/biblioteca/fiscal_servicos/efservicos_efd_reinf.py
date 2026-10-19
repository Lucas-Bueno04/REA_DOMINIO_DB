# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efservicos_efd_reinf (Notas Fiscais de Serviço - EFD Reinf) - módulo fiscal_servicos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efservicos_efd_reinf"
MODULO = "fiscal_servicos"
ENTIDADES = ['efservicos_efd_reinf']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

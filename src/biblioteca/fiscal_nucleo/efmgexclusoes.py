# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmgexclusoes (Exclusoes - Cadastro - MG) - módulo fiscal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmgexclusoes"
MODULO = "fiscal_nucleo"
ENTIDADES = ['efmgexclusoes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

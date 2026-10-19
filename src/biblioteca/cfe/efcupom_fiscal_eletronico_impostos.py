# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcupom_fiscal_eletronico_impostos (Impostos dos CF-e por acumulador) - módulo cfe."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcupom_fiscal_eletronico_impostos"
MODULO = "cfe"
ENTIDADES = ['imposto_cupom_fiscal_eletronico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

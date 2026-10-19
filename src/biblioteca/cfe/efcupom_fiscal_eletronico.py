# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcupom_fiscal_eletronico (Cupons fiscais eletrônicos (CF-e SAT)) - módulo cfe."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcupom_fiscal_eletronico"
MODULO = "cfe"
ENTIDADES = ['cupom_fiscal_eletronico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

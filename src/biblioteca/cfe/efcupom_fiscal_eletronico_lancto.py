# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcupom_fiscal_eletronico_lancto (Lançamentos contábeis dos CF-e) - módulo cfe."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcupom_fiscal_eletronico_lancto"
MODULO = "cfe"
ENTIDADES = ['lancamento_cupom_fiscal_eletronico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

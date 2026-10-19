# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmovimento_ajuste_estadual_sp_lancto (SP - Ajuste Impostos lançados estaduais – Lançamentos contábeis) - módulo fiscal_movimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmovimento_ajuste_estadual_sp_lancto"
MODULO = "fiscal_movimento"
ENTIDADES = ['efmovimento_ajuste_estadual_sp_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

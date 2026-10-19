# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_ro_ajuste_sped_fiscal (Tabela de Relacionamento - RO - Ajuste SPED Fiscal) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_ro_ajuste_sped_fiscal"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_ro_ajuste_sped_fiscal']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

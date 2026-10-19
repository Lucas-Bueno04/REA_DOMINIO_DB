# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efdeducao_pis_cofins_lancto (Restituição, Ressarcimento e Compensação de PIS/COFINS - Deduções - Lançamentos contábeis) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efdeducao_pis_cofins_lancto"
MODULO = "fiscal_outros"
ENTIDADES = ['efdeducao_pis_cofins_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

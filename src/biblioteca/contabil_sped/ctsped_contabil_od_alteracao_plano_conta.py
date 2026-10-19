# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctsped_contabil_od_alteracao_plano_conta (SPED Contábil - Outros Dados - Alteração plano de contas) - módulo contabil_sped."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctsped_contabil_od_alteracao_plano_conta"
MODULO = "contabil_sped"
ENTIDADES = ['ctsped_contabil_od_alteracao_plano_conta']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

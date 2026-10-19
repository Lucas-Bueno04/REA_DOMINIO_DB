# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_vinculo_ncm_nbs_cclasstrib (Tabela de Vínculo de NCM/NBS e cClassTrib) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_vinculo_ncm_nbs_cclasstrib"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_vinculo_ncm_nbs_cclasstrib']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

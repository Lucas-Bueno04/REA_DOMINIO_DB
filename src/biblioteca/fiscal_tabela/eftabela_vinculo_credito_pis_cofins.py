# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_vinculo_credito_pis_cofins (Tabela de vínculos de crédito PIS/COFINS) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_vinculo_credito_pis_cofins"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_vinculo_credito_pis_cofins']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

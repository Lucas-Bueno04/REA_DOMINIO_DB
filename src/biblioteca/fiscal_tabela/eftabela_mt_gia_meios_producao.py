# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_mt_gia_meios_producao (Tabela para os Códigos dos Meios de Produção da GIA do Estado MT) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_mt_gia_meios_producao"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_mt_gia_meios_producao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

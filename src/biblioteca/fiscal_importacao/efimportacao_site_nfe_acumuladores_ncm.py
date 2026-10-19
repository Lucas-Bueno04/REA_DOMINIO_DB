# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportacao_site_nfe_acumuladores_ncm (Configuração da importação da NFe - Tabela de acumuladores e seus NCMs) - módulo fiscal_importacao."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportacao_site_nfe_acumuladores_ncm"
MODULO = "fiscal_importacao"
ENTIDADES = ['efimportacao_site_nfe_acumuladores_ncm']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

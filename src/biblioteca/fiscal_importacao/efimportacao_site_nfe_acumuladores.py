# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportacao_site_nfe_acumuladores (Configuração da importação da NFe - Tabela de acumuladores) - módulo fiscal_importacao."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportacao_site_nfe_acumuladores"
MODULO = "fiscal_importacao"
ENTIDADES = ['efimportacao_site_nfe_acumuladores']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

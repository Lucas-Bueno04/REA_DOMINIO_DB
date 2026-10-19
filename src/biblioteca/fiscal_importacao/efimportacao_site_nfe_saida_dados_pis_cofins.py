# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportacao_site_nfe_saida_dados_pis_cofins (Configuração da importação da NFe - Saída - Dados de PIS/COFINS) - módulo fiscal_importacao."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportacao_site_nfe_saida_dados_pis_cofins"
MODULO = "fiscal_importacao"
ENTIDADES = ['efimportacao_site_nfe_saida_dados_pis_cofins']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

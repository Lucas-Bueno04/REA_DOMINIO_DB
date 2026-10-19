# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_nfe_saida_dados_pis_cofins_dados (Configuração do leiaute NF-e XML do Importador Fixo - Saída - Dados de PIS/COFINS) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_nfe_saida_dados_pis_cofins_dados"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_nfe_saida_dados_pis_cofins_dados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

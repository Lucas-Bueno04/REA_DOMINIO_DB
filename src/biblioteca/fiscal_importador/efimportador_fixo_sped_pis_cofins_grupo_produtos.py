# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_sped_pis_cofins_grupo_produtos (Configuração do leiaute SPED PIS/COFINS do Importador Fixo - Grupo dos produtos) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_sped_pis_cofins_grupo_produtos"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_sped_pis_cofins_grupo_produtos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

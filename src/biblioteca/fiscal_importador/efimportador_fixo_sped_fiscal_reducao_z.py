# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_sped_fiscal_reducao_z (Configuração do leiaute SPED Fiscal do Importador Fixo - Redução Z) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_sped_fiscal_reducao_z"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_sped_fiscal_reducao_z']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

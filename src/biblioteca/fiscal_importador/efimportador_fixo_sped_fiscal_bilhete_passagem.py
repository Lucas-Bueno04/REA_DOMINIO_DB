# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_sped_fiscal_bilhete_passagem (Configuração do leiaute SPED Fiscal do Importador Fixo - Bilhete de Passagem) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_sped_fiscal_bilhete_passagem"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_sped_fiscal_bilhete_passagem']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

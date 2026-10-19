# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoutras_deducoes_pis_cofins (Outras Deduções de PIS/COFINS) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoutras_deducoes_pis_cofins"
MODULO = "fiscal_outros"
ENTIDADES = ['efoutras_deducoes_pis_cofins']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

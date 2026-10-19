# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvspro_estadual_al (Notas Fiscais de Saída - Produtos - Estadual AL) - módulo fiscal_mvspro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvspro_estadual_al"
MODULO = "fiscal_mvspro"
ENTIDADES = ['efmvspro_estadual_al']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

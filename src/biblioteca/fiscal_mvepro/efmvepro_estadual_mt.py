# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvepro_estadual_mt (Notas Fiscais de Entrada - Produtos - Estadual MT) - módulo fiscal_mvepro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvepro_estadual_mt"
MODULO = "fiscal_mvepro"
ENTIDADES = ['efmvepro_estadual_mt']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

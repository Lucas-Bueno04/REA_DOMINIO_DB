# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvepro_base_piscofins (Notas Fiscais de Entrada - Produtos - Bases PIS COFINS) - módulo fiscal_mvepro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvepro_base_piscofins"
MODULO = "fiscal_mvepro"
ENTIDADES = ['efmvepro_base_piscofins']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

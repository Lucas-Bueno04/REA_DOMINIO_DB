# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvepro_extemporaneo_piscofins (Notas Fiscais de Entrada - Produtos - Extemporâneo PIS COFINS) - módulo fiscal_mvepro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvepro_extemporaneo_piscofins"
MODULO = "fiscal_mvepro"
ENTIDADES = ['efmvepro_extemporaneo_piscofins']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

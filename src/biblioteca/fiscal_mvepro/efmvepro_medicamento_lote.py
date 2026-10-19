# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvepro_medicamento_lote (Notas Fiscais de Entrada - Produtos - Medicamento - Lote) - módulo fiscal_mvepro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvepro_medicamento_lote"
MODULO = "fiscal_mvepro"
ENTIDADES = ['efmvepro_medicamento_lote']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

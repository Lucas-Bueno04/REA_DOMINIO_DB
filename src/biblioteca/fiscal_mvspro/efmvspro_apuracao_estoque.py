# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvspro_apuracao_estoque (Notas Fiscais de Saída - Produtos - Apuração de estoque) - módulo fiscal_mvspro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvspro_apuracao_estoque"
MODULO = "fiscal_mvspro"
ENTIDADES = ['efmvspro_apuracao_estoque']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

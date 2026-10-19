# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvspro_simples_nacional_monofasico (Notas Fiscais de Saída - Produtos - Simples Nacional Produto Monofasico) - módulo fiscal_mvspro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvspro_simples_nacional_monofasico"
MODULO = "fiscal_mvspro"
ENTIDADES = ['efmvspro_simples_nacional_monofasico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

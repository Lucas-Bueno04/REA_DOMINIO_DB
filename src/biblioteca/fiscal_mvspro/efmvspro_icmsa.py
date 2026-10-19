# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvspro_icmsa (Notas Fiscais de Saída - Produtos - ICMSA) - módulo fiscal_mvspro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvspro_icmsa"
MODULO = "fiscal_mvspro"
ENTIDADES = ['efmvspro_icmsa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

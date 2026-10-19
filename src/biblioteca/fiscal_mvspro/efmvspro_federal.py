# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvspro_federal (Notas Fiscais de Saida - Produtos - Federal) - módulo fiscal_mvspro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvspro_federal"
MODULO = "fiscal_mvspro"
ENTIDADES = ['efmvspro_federal']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

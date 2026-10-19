# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efgnre_receita_produtos (GNRE - Receita) - módulo fiscal_gnre."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efgnre_receita_produtos"
MODULO = "fiscal_gnre"
ENTIDADES = ['efgnre_receita_produtos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

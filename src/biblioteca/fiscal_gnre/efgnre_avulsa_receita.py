# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efgnre_avulsa_receita (Tabela de receita - GNRE Avulsa) - módulo fiscal_gnre."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efgnre_avulsa_receita"
MODULO = "fiscal_gnre"
ENTIDADES = ['efgnre_avulsa_receita']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

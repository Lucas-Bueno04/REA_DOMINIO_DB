# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_gnre_avulsa_receita (Tabela de receita - GNRE Avulsa) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_gnre_avulsa_receita"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_gnre_avulsa_receita']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

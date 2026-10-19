# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_inss_rb_receita (Saldo dos Impostos - INSS Receita Bruta - Controle de Receita) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_inss_rb_receita"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_inss_rb_receita']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

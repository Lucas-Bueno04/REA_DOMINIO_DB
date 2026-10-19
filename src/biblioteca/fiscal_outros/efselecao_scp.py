# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efselecao_scp (Seleção de Sociedade em Conta de Participação - SCP - Escrita Fiscal) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efselecao_scp"
MODULO = "fiscal_outros"
ENTIDADES = ['efselecao_scp']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

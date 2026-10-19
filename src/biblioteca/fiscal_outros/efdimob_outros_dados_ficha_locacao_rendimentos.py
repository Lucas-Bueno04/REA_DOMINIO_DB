# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efdimob_outros_dados_ficha_locacao_rendimentos (DIMOB - Outras Dados - Ficha de Locação - Rendimentos) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efdimob_outros_dados_ficha_locacao_rendimentos"
MODULO = "fiscal_outros"
ENTIDADES = ['efdimob_outros_dados_ficha_locacao_rendimentos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

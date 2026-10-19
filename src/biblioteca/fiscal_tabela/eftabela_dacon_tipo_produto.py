# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_dacon_tipo_produto (Tabela Auxiliar para o campo Tipo Produto da tabela de Produtos) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_dacon_tipo_produto"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_dacon_tipo_produto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

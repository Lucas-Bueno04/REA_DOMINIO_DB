# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lroperacao_receita (Cadastro Operações de Receita) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lroperacao_receita"
MODULO = "contabil_outros"
ENTIDADES = ['lroperacao_receita']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

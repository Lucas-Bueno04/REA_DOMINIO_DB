# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foremuneracao_variavel (Descrição da Remuneração Variável.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foremuneracao_variavel"
MODULO = "pessoal_outros"
ENTIDADES = ['foremuneracao_variavel']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

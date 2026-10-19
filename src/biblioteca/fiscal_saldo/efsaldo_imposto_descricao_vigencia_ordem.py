# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsaldo_imposto_descricao_vigencia_ordem (Tela de Apuração de Impostos - Layouts - Ordem das colunas) - módulo fiscal_saldo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsaldo_imposto_descricao_vigencia_ordem"
MODULO = "fiscal_saldo"
ENTIDADES = ['efsaldo_imposto_descricao_vigencia_ordem']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

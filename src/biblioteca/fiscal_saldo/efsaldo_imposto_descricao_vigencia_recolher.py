# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsaldo_imposto_descricao_vigencia_recolher (Tela de Apuração de Impostos - Recolher) - módulo fiscal_saldo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsaldo_imposto_descricao_vigencia_recolher"
MODULO = "fiscal_saldo"
ENTIDADES = ['efsaldo_imposto_descricao_vigencia_recolher']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

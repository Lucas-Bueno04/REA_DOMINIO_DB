# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotabela_calculo_irrf_participacao_lucros_faixas (Faixas da tabela de cálculo de IRRF sobre participação nos lucros.) - módulo pessoal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotabela_calculo_irrf_participacao_lucros_faixas"
MODULO = "pessoal_tabela"
ENTIDADES = ['fotabela_calculo_irrf_participacao_lucros_faixas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

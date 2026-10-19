# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoutrosdados_planejamento_tributario_custos_despesas_lucro_real (Outros Dados - Planejamento Tributário - Custos e Despesas (Lucro Real)) - módulo fiscal_outrosdados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoutrosdados_planejamento_tributario_custos_despesas_lucro_real"
MODULO = "fiscal_outrosdados"
ENTIDADES = ['efoutrosdados_planejamento_tributario_custos_despesas_lucro_x']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

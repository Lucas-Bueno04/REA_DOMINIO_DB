# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoutrosdados_planejamento_tributario_cfops_considerados (Outros Dados - Planejamento Tributário - CFOPs considerados para o cálculo (debito e credito)) - módulo fiscal_outrosdados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoutrosdados_planejamento_tributario_cfops_considerados"
MODULO = "fiscal_outrosdados"
ENTIDADES = ['efoutrosdados_planejamento_tributario_cfops_considerados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

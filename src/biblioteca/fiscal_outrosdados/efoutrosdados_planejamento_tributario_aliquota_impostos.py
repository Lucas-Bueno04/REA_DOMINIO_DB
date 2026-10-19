# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoutrosdados_planejamento_tributario_aliquota_impostos (Outros Dados - Planejamento Tributário - Aliquota dos Impostos) - módulo fiscal_outrosdados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoutrosdados_planejamento_tributario_aliquota_impostos"
MODULO = "fiscal_outrosdados"
ENTIDADES = ['efoutrosdados_planejamento_tributario_aliquota_impostos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

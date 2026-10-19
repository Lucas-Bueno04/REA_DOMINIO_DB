# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoutrosdados_planejamento_tributario_percentual_rb_simples_nacional (Outros Dados - Planejamento Tributario - Percentual de Receita Bruta calculo Simples Nacional) - módulo fiscal_outrosdados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoutrosdados_planejamento_tributario_percentual_rb_simples_nacional"
MODULO = "fiscal_outrosdados"
ENTIDADES = ['efoutrosdados_planejamento_tributario_percentual_rb_simples']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

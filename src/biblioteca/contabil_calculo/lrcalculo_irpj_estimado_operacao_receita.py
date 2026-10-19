# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrcalculo_irpj_estimado_operacao_receita (Cálculo do Lalur - Imposto IRPJ Estimado - Detalhamento de Vendas, Serviços e Não Operacional) - módulo contabil_calculo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrcalculo_irpj_estimado_operacao_receita"
MODULO = "contabil_calculo"
ENTIDADES = ['lrcalculo_irpj_estimado_operacao_receita']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

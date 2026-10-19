# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmovacu_compensacoes (Outros Movimentos - Impostos Calculados - Outras compensacoes) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmovacu_compensacoes"
MODULO = "fiscal_outros"
ENTIDADES = ['efmovacu_compensacoes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

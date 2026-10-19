# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmovacu_detalhamento_retencoes (Detalhamento das retenções dos movimentos de acumuladores) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmovacu_detalhamento_retencoes"
MODULO = "fiscal_outros"
ENTIDADES = ['efmovacu_detalhamento_retencoes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

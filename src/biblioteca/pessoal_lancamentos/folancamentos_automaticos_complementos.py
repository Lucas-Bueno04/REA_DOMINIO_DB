# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela folancamentos_automaticos_complementos (Lançamentos automáticos de eventos para complementos de cálculos) - módulo pessoal_lancamentos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "folancamentos_automaticos_complementos"
MODULO = "pessoal_lancamentos"
ENTIDADES = ['folancamentos_automaticos_complementos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

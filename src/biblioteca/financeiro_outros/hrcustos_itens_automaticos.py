# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrcustos_itens_automaticos (Itens de custos automáticos pré definidos) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrcustos_itens_automaticos"
MODULO = "financeiro_outros"
ENTIDADES = ['hrcustos_itens_automaticos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

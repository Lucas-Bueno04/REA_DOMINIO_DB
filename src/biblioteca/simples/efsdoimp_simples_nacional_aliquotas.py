# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_simples_nacional_aliquotas (Alíquotas efetivas do Simples Nacional por anexo) - módulo simples."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_simples_nacional_aliquotas"
MODULO = "simples"
ENTIDADES = ['aliquota_simples_nacional']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

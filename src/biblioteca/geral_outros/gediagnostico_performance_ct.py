# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gediagnostico_performance_ct (Diagnóstico de Performance (retenção 90 dias)) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gediagnostico_performance_ct"
MODULO = "geral_outros"
ENTIDADES = ['gediagnostico_performance_ct']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

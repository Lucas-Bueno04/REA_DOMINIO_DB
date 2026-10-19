# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_simples_nacional (Apuração mensal do Simples Nacional) - módulo simples."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_simples_nacional"
MODULO = "simples"
ENTIDADES = ['apuracao_simples_nacional']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

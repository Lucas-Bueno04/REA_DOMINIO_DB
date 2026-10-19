# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomediascalc_simulacao (Médias da simulação da rescisão) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomediascalc_simulacao"
MODULO = "pessoal_outros"
ENTIDADES = ['fomediascalc_simulacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

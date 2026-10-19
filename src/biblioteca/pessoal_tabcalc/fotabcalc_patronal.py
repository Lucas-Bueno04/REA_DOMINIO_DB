# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotabcalc_patronal (Tabela de Contribuição Sindical Patronal) - módulo pessoal_tabcalc."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotabcalc_patronal"
MODULO = "pessoal_tabcalc"
ENTIDADES = ['fotabcalc_patronal']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

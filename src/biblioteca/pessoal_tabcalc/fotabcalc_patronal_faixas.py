# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotabcalc_patronal_faixas (Tabela de Contribuição Sindical Patronal - Faixas) - módulo pessoal_tabcalc."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotabcalc_patronal_faixas"
MODULO = "pessoal_tabcalc"
ENTIDADES = ['fotabcalc_patronal_faixas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotabcalcirrf_faixas (Tabela de IRRF - Faixas) - módulo pessoal_tabcalcirrf."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotabcalcirrf_faixas"
MODULO = "pessoal_tabcalcirrf"
ENTIDADES = ['fotabcalcirrf_faixas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

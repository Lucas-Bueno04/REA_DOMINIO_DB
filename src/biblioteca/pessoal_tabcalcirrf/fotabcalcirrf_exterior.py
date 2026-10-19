# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotabcalcirrf_exterior (Tabela de IRRF para residentes no exterior.) - módulo pessoal_tabcalcirrf."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotabcalcirrf_exterior"
MODULO = "pessoal_tabcalcirrf"
ENTIDADES = ['fotabcalcirrf_exterior']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotabcalcirrf_exterior_faixas (Faixas da tabela de IRRF para residentes no exterior.) - módulo pessoal_tabcalcirrf."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotabcalcirrf_exterior_faixas"
MODULO = "pessoal_tabcalcirrf"
ENTIDADES = ['fotabcalcirrf_exterior_faixas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

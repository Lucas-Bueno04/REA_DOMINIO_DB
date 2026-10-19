# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotabcalcirrf_faixas_complemento (Tabela de faixas para complementar o IRRF a partir de 01/2026 conforme LEI Nº 1,087 DE 2025) - módulo pessoal_tabcalcirrf."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotabcalcirrf_faixas_complemento"
MODULO = "pessoal_tabcalcirrf"
ENTIDADES = ['fotabcalcirrf_faixas_complemento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

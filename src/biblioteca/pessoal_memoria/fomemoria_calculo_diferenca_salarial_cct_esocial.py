# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomemoria_calculo_diferenca_salarial_cct_esocial (Memória de cálculo do cálculo de diferença salarial CCT com algumas considerações do eSocial) - módulo pessoal_memoria."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomemoria_calculo_diferenca_salarial_cct_esocial"
MODULO = "pessoal_memoria"
ENTIDADES = ['fomemoria_calculo_diferenca_salarial_cct_esocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

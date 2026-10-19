# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomemoria_calculo_inss (Memória de cálculo do INSS) - módulo pessoal_memoria."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomemoria_calculo_inss"
MODULO = "pessoal_memoria"
ENTIDADES = ['fomemoria_calculo_inss']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

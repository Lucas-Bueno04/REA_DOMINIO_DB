# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomemoria_calculo_salario_indenizacao_mp_936 (Memória de cálculo da indenização MP 936.) - módulo pessoal_memoria."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomemoria_calculo_salario_indenizacao_mp_936"
MODULO = "pessoal_memoria"
ENTIDADES = ['fomemoria_calculo_salario_indenizacao_mp_936']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

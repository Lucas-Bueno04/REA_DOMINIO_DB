# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focadbases (Cadastro de bases de cálculo da folha) - módulo folha_calculo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focadbases"
MODULO = "folha_calculo"
ENTIDADES = ['cadastro_base_calculo_folha']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

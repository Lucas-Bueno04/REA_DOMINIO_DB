# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foferias_coletivas (CALCULOS DE FERIAS COLETIVAS) - módulo pessoal_ferias."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foferias_coletivas"
MODULO = "pessoal_ferias"
ENTIDADES = ['foferias_coletivas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

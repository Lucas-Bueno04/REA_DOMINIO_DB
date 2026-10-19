# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geraexecutar_empresas_opcoes_contabilidade (Informações da contabilidade por empresa utilizados na rotina automatica) - módulo geral_raexecutar."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geraexecutar_empresas_opcoes_contabilidade"
MODULO = "geral_raexecutar"
ENTIDADES = ['geraexecutar_empresas_opcoes_contabilidade']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

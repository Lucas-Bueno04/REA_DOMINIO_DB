# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gescp_vigencia_informativos (Sociedade em Conta de Participação - SCP - Vigência Informativos) - módulo geral_scp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gescp_vigencia_informativos"
MODULO = "geral_scp"
ENTIDADES = ['gescp_vigencia_informativos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

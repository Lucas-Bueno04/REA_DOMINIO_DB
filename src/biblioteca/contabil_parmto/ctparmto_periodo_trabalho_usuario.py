# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctparmto_periodo_trabalho_usuario (Parametros - Período de trabalho por usuário) - módulo contabil_parmto."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctparmto_periodo_trabalho_usuario"
MODULO = "contabil_parmto"
ENTIDADES = ['ctparmto_periodo_trabalho_usuario']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

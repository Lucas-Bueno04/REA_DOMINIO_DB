# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctparmto_filial_api_conta_azul (Seleção de empresas filiais para o envio api conta azul) - módulo contabil_parmto."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctparmto_filial_api_conta_azul"
MODULO = "contabil_parmto"
ENTIDADES = ['ctparmto_filial_api_conta_azul']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

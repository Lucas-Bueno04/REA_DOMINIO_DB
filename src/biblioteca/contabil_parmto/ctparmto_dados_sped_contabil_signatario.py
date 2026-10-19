# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctparmto_dados_sped_contabil_signatario (Dados da Assinaturas do registro J930 do SPED CONTABIL) - módulo contabil_parmto."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctparmto_dados_sped_contabil_signatario"
MODULO = "contabil_parmto"
ENTIDADES = ['ctparmto_dados_sped_contabil_signatario']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

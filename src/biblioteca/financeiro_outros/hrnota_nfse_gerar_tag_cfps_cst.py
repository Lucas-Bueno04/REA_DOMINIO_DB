# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrnota_nfse_gerar_tag_cfps_cst (Tabela de validação para CFPS x CST) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrnota_nfse_gerar_tag_cfps_cst"
MODULO = "financeiro_outros"
ENTIDADES = ['hrnota_nfse_gerar_tag_cfps_cst']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

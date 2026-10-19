# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efam_codigo_tributacao_produto (AM - Código de Tributação do Produto - DIA) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efam_codigo_tributacao_produto"
MODULO = "fiscal_outros"
ENTIDADES = ['efam_codigo_tributacao_produto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

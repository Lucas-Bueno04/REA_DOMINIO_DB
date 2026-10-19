# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efempreendimentos_imobiliarios_contratos_venda_cliente (Empreendimentos Imobiliários - Contratos de Venda - Cliente) - módulo fiscal_empreendimentos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efempreendimentos_imobiliarios_contratos_venda_cliente"
MODULO = "fiscal_empreendimentos"
ENTIDADES = ['efempreendimentos_imobiliarios_contratos_venda_cliente']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

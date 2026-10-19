# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efempreendimentos_imobiliarios_contratos_venda_cliente_alteracao (Empreendimentos Imobiliários - Contratos de Venda - Alteraçõs de Clientes) - módulo fiscal_empreendimentos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efempreendimentos_imobiliarios_contratos_venda_cliente_alteracao"
MODULO = "fiscal_empreendimentos"
ENTIDADES = ['efempreendimentos_imobiliarios_contratos_venda_cliente_alter']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

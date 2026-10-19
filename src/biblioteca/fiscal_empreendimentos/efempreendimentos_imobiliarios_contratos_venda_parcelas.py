# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efempreendimentos_imobiliarios_contratos_venda_parcelas (Empreendimentos imobiliários - Contratos de venda - Parcelas) - módulo fiscal_empreendimentos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efempreendimentos_imobiliarios_contratos_venda_parcelas"
MODULO = "fiscal_empreendimentos"
ENTIDADES = ['efempreendimentos_imobiliarios_contratos_venda_parcelas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

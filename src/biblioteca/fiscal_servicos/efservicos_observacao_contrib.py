# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efservicos_observacao_contrib (Notas Fiscais de Serviços - Obseração de interesse do contribuinte) - módulo fiscal_servicos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efservicos_observacao_contrib"
MODULO = "fiscal_servicos"
ENTIDADES = ['efservicos_observacao_contrib']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

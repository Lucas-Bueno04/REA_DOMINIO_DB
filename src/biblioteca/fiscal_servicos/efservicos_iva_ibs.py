# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efservicos_iva_ibs (Notas Fiscais de Serviços - IVA IBS) - módulo fiscal_servicos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efservicos_iva_ibs"
MODULO = "fiscal_servicos"
ENTIDADES = ['efservicos_iva_ibs']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

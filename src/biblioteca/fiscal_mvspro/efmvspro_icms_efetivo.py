# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvspro_icms_efetivo (Notas Fiscais de Saída - Produtos - ICMS Efetivo Geral) - módulo fiscal_mvspro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvspro_icms_efetivo"
MODULO = "fiscal_mvspro"
ENTIDADES = ['efmvspro_icms_efetivo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

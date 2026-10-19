# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efservicos_observacao_fisco (Notas Fiscais de Serviços - Observação de interesse do fisco) - módulo fiscal_servicos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efservicos_observacao_fisco"
MODULO = "fiscal_servicos"
ENTIDADES = ['efservicos_observacao_fisco']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

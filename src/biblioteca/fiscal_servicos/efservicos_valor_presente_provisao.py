# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efservicos_valor_presente_provisao (Notas Fiscais de Servico - Valor Presente Provisao) - módulo fiscal_servicos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efservicos_valor_presente_provisao"
MODULO = "fiscal_servicos"
ENTIDADES = ['efservicos_valor_presente_provisao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

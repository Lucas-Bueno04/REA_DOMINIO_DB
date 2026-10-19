# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradas_valor_presente_provisao (Notas Fiscais de Entrada - Valor Presente Provisao) - módulo fiscal_entradas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradas_valor_presente_provisao"
MODULO = "fiscal_entradas"
ENTIDADES = ['efentradas_valor_presente_provisao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

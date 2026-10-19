# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradas_info_pag (Notas Fiscais de Entradas - Informação Pagamento) - módulo fiscal_entradas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradas_info_pag"
MODULO = "fiscal_entradas"
ENTIDADES = ['efentradas_info_pag']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

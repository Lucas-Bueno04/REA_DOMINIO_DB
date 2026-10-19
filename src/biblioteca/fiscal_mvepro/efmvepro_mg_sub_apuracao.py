# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvepro_mg_sub_apuracao (Notas Fiscais de Entrada - Produtos - MG Sub Apuração) - módulo fiscal_mvepro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvepro_mg_sub_apuracao"
MODULO = "fiscal_mvepro"
ENTIDADES = ['efmvepro_mg_sub_apuracao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

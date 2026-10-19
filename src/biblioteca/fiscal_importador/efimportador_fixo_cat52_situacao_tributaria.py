# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_cat52_situacao_tributaria (Configuração do leiaute CAT52 do Importador Fixo - Situação tributária) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_cat52_situacao_tributaria"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_cat52_situacao_tributaria']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

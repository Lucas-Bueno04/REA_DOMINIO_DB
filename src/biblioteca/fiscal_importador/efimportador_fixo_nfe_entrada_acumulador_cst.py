# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_nfe_entrada_acumulador_cst (Configuração do leiaute NF-e XML do Importador Fixo - Entrada - Acumulador - CST) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_nfe_entrada_acumulador_cst"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_nfe_entrada_acumulador_cst']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_cfe_saida_acumulador_produto (Configuração do leiaute CF-e XML do Importador Fixo - Saída - Acumulador - Produto) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_cfe_saida_acumulador_produto"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_cfe_saida_acumulador_produto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

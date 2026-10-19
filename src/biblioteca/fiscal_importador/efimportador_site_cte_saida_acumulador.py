# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_site_cte_saida_acumulador (Configuração da importação do CT-e pelo site da Receita Federal - Saída - Acumulador) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_site_cte_saida_acumulador"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_site_cte_saida_acumulador']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]

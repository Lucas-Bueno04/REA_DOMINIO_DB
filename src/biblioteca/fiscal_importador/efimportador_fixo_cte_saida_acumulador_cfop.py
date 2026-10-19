# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_cte_saida_acumulador_cfop (Configuração do leiaute CT-e XML do Importador Fixo - Saída - Acumulador - CFOP) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_cte_saida_acumulador_cfop"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_cte_saida_acumulador_cfop']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
